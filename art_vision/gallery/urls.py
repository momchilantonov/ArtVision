from art_vision.gallery.views import get_album
from django.urls import path


urlpatterns = [
    path('album/<int:pk>', get_album, name='get album')
]