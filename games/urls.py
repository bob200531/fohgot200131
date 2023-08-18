from django.urls import path,include
from .views import *
# from rest_framework import routers

# router = routers.DefaultRouter()
urlpatterns = [
    path('genre-list/', MyModelCreateView.as_view(),name = 'genre-list'),
    path('genre-detail/<int:pk>/',MyModelUpdateView.as_view(),name='genre-detail'),
    path('colllect/',GameCollectionGenericFilters.as_view(),name='colllect'),
    path('search-game/', GameSearch.as_view(),name='search-game'),
    path('purchaseList/',PurchaseList.as_view(),name='purchaseList')

    # path('', include(router.urls)),
]
