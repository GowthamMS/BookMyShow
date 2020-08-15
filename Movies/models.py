from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    cast = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=20, null=True, blank=True)
    release_date = models.DateField(help_text='mm/dd/yyyy')

    def __str__(self):
        return self.name
