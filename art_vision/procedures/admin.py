from art_vision.procedures.models import Procedure
from django.contrib import admin


@admin.register(Procedure)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'price']