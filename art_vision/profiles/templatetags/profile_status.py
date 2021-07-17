from django.template import Library
from art_vision.profiles.models import Profile


register = Library()


@register.inclusion_tag('profile/status.html', takes_context=True)
def show_profile_status(context):
    user_id = context.request.user.id
    profile = Profile.objects.get(pk=user_id)
    return {
        'is_completed': profile.is_completed,
    }