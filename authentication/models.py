from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.models import TimeStampedModel


class CityLocation(TimeStampedModel):
    name = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Name"
    )

    def __str__(self):
        return str(self.name)


class CustomUser(AbstractUser):
    city_location = models.ForeignKey(
        CityLocation, null=True, blank=True, on_delete=models.SET_NULL)
