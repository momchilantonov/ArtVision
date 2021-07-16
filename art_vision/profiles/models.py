from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='profile/%Y/%m/%d')
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
