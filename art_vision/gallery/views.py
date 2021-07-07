from art_vision.core.views import get_obj_by_id
from art_vision.gallery.models import Album, Image
from django.shortcuts import render


def show_album(req, pk):
    album = get_obj_by_id(Album, pk)
    images = album.image_set.all()
    context = {
        'album': album,
        'images': images,
        
    }
    return render(req, 'gallery/show_album.html', context)