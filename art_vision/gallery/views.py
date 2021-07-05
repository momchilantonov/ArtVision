from art_vision.gallery.models import Album
from django.shortcuts import render

# Create your views here.
def show_albums(req):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(req, 'body.html', context)