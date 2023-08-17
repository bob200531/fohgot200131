"""
URL configuration for nesteam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from games.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'genreset',GenreVieWSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('games-list/',games_list,name='games-list'),
    path('game-lst/',game_lst,name='games-list'),
    path('game-create/',GamesCrateMixin.as_view(),name='game-create'),
    path('video-cretate/',ViedoGameCreate.as_view(),name='video-cretate/'),
    path('videogame-destroy/<int:id>/',VideoDetail.as_view(),name='videogame-destroy'),
    path('snippets/', VideoGameList.as_view()),
    path('snippets/<int:pk>/', GamesDetail.as_view()),
    path('studio-list/',StudioListGeneric.as_view(),name='studio-list'),
    path('studio-create/', StudioGenericCreate.as_view() ,name='studio-create',),
    path('player-api/',PlayerAPIGeneric.as_view(),name='player-api'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('user-list/', UserListView.as_view(), name='user-list'),
    path('users-detail/<int:pk>/', UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('users-manual/',include('userapp.urls')),
    path('genre/',include('games.urls')),
]
urlpatterns += router.urls

# urlpatterns = format_suffix_patterns(urlpatterns)