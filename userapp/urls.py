from django.urls import path,include
from .views import *
from django.contrib.auth.models import User



urlpatterns = [
    path('manual-lst-users/',UsersManualList,name='manual-lst-users'),
    path('manual-detail-users/<int:pk>/' ,UsersManyalDetail, name='manual-detail-users/')
]