from art_vision.core.views import get_obj_by_id
from art_vision.gallery.models import Album, Image
from django.shortcuts import render


def get_album(req, pk):
    album = get_obj_by_id(Album, pk)
    images = Image.objects.filter(album=album)
    context = {
        'album': album,
        'images': images,
    }
    return render(req, 'gallery/show_album.html', context)