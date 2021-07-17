from django.template import Library
from art_vision.gallery.models import Album
from art_vision.core.views import get_all_objs


register = Library()


@register.inclusion_tag('core/albums_dropdown.html')
def show_albums_dropdown():
    albums = get_all_objs(Album)
    return {
        'albums': albums,
    }


# @register.inclusion_tag('core/procedures_dropdown.html')
# def show_procedures_dropdown():
#     procedures = get_all_objs(Procedure)
#     context = {
#         'procedures': procedures
#     }
#     return context
