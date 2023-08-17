from rest_framework import  filters

from .models import  GameCollection

class  GameCollectionFilter(filters.models):
    model = GameCollection
    fields = [
         'name'
    ]