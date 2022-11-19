# -*- coding: utf8 -*-
from django.db.models import Count, Q
from django.http import JsonResponse
from rest_framework.generics import *
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


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        ad_cat = request.GET.get('cat')
        if ad_cat:
            self.queryset = self.queryset.filter(category__id__exact=ad_cat)

        ad_name = request.GET.get('text')
        if ad_name:
          self.queryset = self.queryset.filter(name__icontains=ad_name)

        ad_city = request.GET.get('location')
        if ad_city:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=ad_city)

        price_from = request.GET.get('price_from', 0)
        price_to = request.GET.get('price_to', 100000)
        if price_from or price_to:
            self.queryset = self.queryset.filter(
                price__range=[price_from,price_to])

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateImageSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserAdDetailView(ListAPIView):
    queryset = User.objects.annotate(total_ads=Count('ad', filter=Q(ad__is_published=True)))
    serializer_class = UserAdSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    # filterset_fields = ['category', 'name', 'price']

