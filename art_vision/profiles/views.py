from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from art_vision.profiles.models import Profile
from art_vision.profiles.forms import ProfileForm


@login_required
def profile_details(req):
    profile = Profile.objects.get(pk=req.user.id)
    if req.method == "POST":
        form = ProfileForm(req.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(req, 'profile/details.html', context)