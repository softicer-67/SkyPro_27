# -*- coding: utf8 -*-
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [
        ('member', 'Пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Админ')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLES, default='member')
    age = models.SmallIntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Ad(models.Model):
    name = models.CharField('Объявление', max_length=200)
    author = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE, null=True, verbose_name='Продавец')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0)
    description = models.TextField('Описание', max_length=2000, blank=True)
    image = models.ImageField('Фото', upload_to='images/', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField('Опубликовано')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
