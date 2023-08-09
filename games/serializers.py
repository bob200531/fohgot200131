from rest_framework import serializers
from .models import Games,Studio,PlayerAPI
from django.contrib.auth.models import User, Group

class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"

class StudioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

class PlayerAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = PlayerAPI
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GamesSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'