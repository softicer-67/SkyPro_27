from django.contrib import admin
from .models import Category, Ad, User, Location


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'image']
    search_fields = ['name', 'price']


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Location)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

