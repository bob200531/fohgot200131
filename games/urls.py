from django.urls import path,include
from .views import *
urlpatterns = [
    path('genre-list/', MyModelCreateView.as_view(),name = 'genre-list')
]
