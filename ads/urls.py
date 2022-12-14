from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from ads import views
from ads.views import LocationViewSet, CategoryViewSet, UserViewSet, AdViewSet

router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'cat', CategoryViewSet)
router.register(r'user', UserViewSet)
router.register(r'ad', AdViewSet)


urlpatterns = [
    path("", views.index),
    path("", include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
