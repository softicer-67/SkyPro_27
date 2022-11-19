from rest_framework import serializers
from .models import *


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='id')
    category = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Ad
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # location = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'
