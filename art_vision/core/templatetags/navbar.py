from art_vision.gallery.models import Album
from art_vision.core.views import get_all_objs
from django import template


register = template.Library()


@register.inclusion_tag('core/albums_dropdown.html')
def show_albums_dropdown():
    return {'albums': get_all_objs(Album)}
        
    


# @register.inclusion_tag('core/procedures_dropdown.html')
# def show_procedures_dropdown():
#     procedures = get_all_objs(Procedure)
#     context = {
#         'procedures': procedures
#     }
#     return context