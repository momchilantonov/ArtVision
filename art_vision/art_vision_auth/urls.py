from art_vision.art_vision_auth.views import sign_in, sign_out, sign_up
from django.urls import path

urlpatterns = [
    path('sign-up/', sign_up, name='sign up'),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
]