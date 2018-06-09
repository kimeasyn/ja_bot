from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(WebDust)
class DustAdmin(admin.ModelAdmin):
    list_display = ['status', 'dust_level', 'micro_dust_level', 'save_at']


@admin.register(NaverSearch)
class NaverAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'title', 'link', 'save_at']


@admin.register(ApiWeather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ['temp', 'status', 'humidity', 'save_at']


@admin.register(WebMusic)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['rank', 'title', 'singer', 'save_at']


@admin.register(WebNews)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'save_at']


@admin.register(WebWebtoon)
class WebtoonAdmin(admin.ModelAdmin):
    list_display = ['title', 'save_at']


@admin.register(WebStock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['company', 'price', 'save_at']

