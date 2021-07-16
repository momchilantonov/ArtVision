from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def sign_up(req):
    if req.POST:
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(req, 'auth/sign_up.html', context)



def sign_in(req):
    user = authenticate(username='momchil', password='papa1234')
    login(req, user)
    return redirect('home page')


def sign_out(req):
    logout(req)
    return redirect('home page')