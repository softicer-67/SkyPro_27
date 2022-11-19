from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from ads import views
from ads.views import LocationViewSet, CategoryViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'cat', CategoryViewSet)
router.register(r'user', UserViewSet)


urlpatterns = [
    path("", views.index),
    path('ad/', views.AdListView.as_view()),
    path("", include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
