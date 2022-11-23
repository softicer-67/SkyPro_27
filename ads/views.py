# -*- coding: utf8 -*-
from django.http import JsonResponse
from rest_framework.response import Response

from ads.serializers import *
from rest_framework.viewsets import ModelViewSet


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def list(self, request, *args, **kwargs):
        ad_cat = request.GET.get('cat')
        if ad_cat:
            self.queryset = self.queryset.filter(category__id__in=ad_cat)

        ad_name = request.GET.get('text')
        if ad_name:
            self.queryset = self.queryset.filter(name__icontains=ad_name)

        ad_city = request.GET.get('location')
        if ad_city:
            self.queryset = self.queryset.filter(author__location__name__icontains=ad_city)

        price_from = request.GET.get('price_from', 0)
        price_to = request.GET.get('price_to', 100000)
        if price_from or price_to:
            self.queryset = self.queryset.filter(price__range=[price_from, price_to])

        serial = self.get_serializer(self.queryset, many=True)
        return Response(serial.data)
