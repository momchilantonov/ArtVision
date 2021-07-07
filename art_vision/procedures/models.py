from django.db import models


class Procedure(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'procedures'