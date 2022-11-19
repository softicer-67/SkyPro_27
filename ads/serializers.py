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


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserAdSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField()
    location = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        slug_field='name',
        many=True,
        queryset=Location.objects.all()
    )

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop('location')
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc in self._location:
            obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(obj)
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        slug_field='name',
        many=True,
        queryset=Location.objects.all()
    )

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('location')
        super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for location in self._locations:
            obj, _ = Location.objects.get_or_create(name=location)
            user.location.clear()
            user.location.add(obj)
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class AdUpdateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'image']
