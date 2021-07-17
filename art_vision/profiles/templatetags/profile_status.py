from django import template
from art_vision.profiles.forms import ProfileForm


register = template.library()


@register.inclusion_tag('profile/status.html', takes_context=True)
def profile_status(context):
    user_id = context.req.user.id
    profile = ProfileForm.objects.get(pk=user_id)
    return {
        'is_completed': profile.is_completed,
    }