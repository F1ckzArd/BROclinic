from django.db import models
from utils.models import TimeStampedModel
from martor.models import MartorField


class Article(TimeStampedModel):
    title = models.CharField(max_length=150, unique=True, verbose_name="Title")
    description = models.TextField(
        blank=True, null=True, verbose_name="Description")
    image = models.ImageField(
        blank=True, null=True, upload_to="docs_images", verbose_name="Image"
    )
    content = MartorField(verbose_name="Content")

    def __str__(self):
        return str(self.title)
