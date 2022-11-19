from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from ads import views
from rest_framework import routers
from ads.views import LocationViewSet, CategoryViewSet


router = routers.SimpleRouter()
router.register('location', LocationViewSet)
router.register('cat', CategoryViewSet)


urlpatterns = [
    path("", views.index),

    path('ad/', views.AdListView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/image/', views.AdImageView.as_view()),
    path('ad/<int:pk>', views.AdDetailView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),

    path('user/', views.UserListView.as_view()),
    path('user/Z/', views.UserAdDetailView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
