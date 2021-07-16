from art_vision.art_vision_auth.forms import SignInForm, SignUpForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


def sign_up(req):
    if req.POST:
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(req, 'auth/sign_up.html', context)


def sign_in(req):
    if req.method == 'POST':
        form = SignInForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('home page')
    else:
        form = SignInForm()
    context = {
        'form': form,
    }
    return render(req, 'auth/sign_in.html', context)


def sign_out(req):
    logout(req)
    return redirect('home page')
