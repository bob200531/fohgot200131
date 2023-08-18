from django.shortcuts import render
from .models import *
from .serializers import *
from django.http.response import HttpResponse,JsonResponse
from django.http import Http404
from django.db.models import Q

from rest_framework import generics,viewsets,permissions,mixins,filters
from rest_framework import status
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.models import User, Group
from rest_framework.reverse import reverse
#pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
#auth
from django.contrib.auth.models import User
# Create your views here.

#Фильтрация по текущему пользователю


def games_list(request):
    games_lst = Games.objects.all()
    serializers = GameSerializers(games_lst,many=True)
    data = serializers.data
    return JsonResponse(data,safe=False)
class StudioListGeneric(generics.ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializers
class ViedoGameCreate(generics.CreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializerCreate

class StudioGenericCreate(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializerCreate

#CreateAPIView
class PlayerAPIGeneric(generics.ListAPIView):
    queryset = PlayerAPI.objects.all()
    serializer_class = PlayerAPISerializers
class VideoDetail(generics.RetrieveDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializers
    lookup_field = 'id'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GamesCrateMixin(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Games.objects.all()
    serializer_class =GamesSerializerCreate


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenreVieWSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

@api_view(['GET', 'POST'])
def game_lst(request):
    if request.method == 'GET':
        game_spicok = Games.objects.all()
        serializers = GameSerializers(game_spicok,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = GameSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)

class VideoGameList(APIView):
    def get(self,request,format=None):
        videogame_lst = Games.objects.all()
        serializers = GameSerializers(videogame_lst,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers =GameSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)


class GamesDetail(APIView):
    def get_objects_games_list(self,pk):
        try:
            return Games.objects.get(pk=pk)
        except Games.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        videogame_lst = self.get_objects_games_list(pk)
        serializers = GameSerializers(videogame_lst)
        return Response(serializers.data)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerInfo

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerInfo

    def perform_create(self,serializer):
        serializer.save(name=self.request.user)


class MyModelCreateView(mixins.CreateModelMixin,generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def post(self, request, *args, **kwargs): # создание формы
        return self.create(request, *args, **kwargs)
class MyModelUpdateView(mixins.UpdateModelMixin,generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def put(self, request, *args, **kwargs):# изменение
        return self.update(request, *args, **kwargs)
    
class GameCollectionGenericFilters(generics.ListAPIView):
    queryset = GameCollection.objects.all()
    serializer_class = GameCollectionSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # filter_backends = [filters.GameCollectionGenericFilters]

class GameSearch(generics.ListAPIView):
     queryset = Games.objects.all()
     serializer_class = GameSerializers
     filter_backends = [filters.SearchFilter,filters.OrderingFilter]
     search_fields = ['name','year',]
     ordering_fields = ['name', 'year']
     # поиск по со связью ключей
     # почему жанр отрисовывается 

    #  def get_queryset(self):
    #       queryset = Games.objects.all()
    #       search_query = self.request.query_params.get('search', None)
    #       if search_query is not None:
    #           queryset = queryset.filter((Q(name__icontains=search_query) | Q(genre__name__icontains=search_query)))
    #       return queryset
    

#  @api_view(['GET'])
#  def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })

class PurchaseList(generics.ListAPIView):
    serializer_class = Games

    def get_queryset(self):
        user = self.request.user
        return Games.objects.filter(purchaser=user)
