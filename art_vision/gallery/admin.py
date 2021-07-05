from art_vision.gallery.models import Album, Image
from django.contrib import admin


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Image)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'album', 'image']
    