from art_vision.gallery.views import show_album
from django.urls import path


urlpatterns = [
    path('album/<int:pk>', show_album, name='get album')
]