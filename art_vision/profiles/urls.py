from art_vision.profiles.views import profile_details
from django.urls import path
from art_vision.profiles import signals


urlpatterns = [
    path('', profile_details, name='profile details'),
]
