from art_vision.gallery.models import Album
from django.shortcuts import render


def get_obj_by_id(obj, pk):
    return obj.objects.get(pk=pk)


def get_all_objs(obj):
    return obj.objects.all()


def get_first_obj(obj):
    return obj.objects.first()


def home_page(req):
    return render(req, 'core/home_page.html')
