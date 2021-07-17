from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    email = models.EmailField(
        blank=True,
    )
    image = models.ImageField(
        upload_to='profile/%Y/%m/%d',
        blank=True,
    )
    is_completed = models.BooleanField(
        default=False,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
