from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'albums'


class Image(models.Model):
    title = models.CharField(max_length=20)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'images'