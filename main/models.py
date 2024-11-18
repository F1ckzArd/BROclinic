from django.db import models
from utils.models import TimeStampedModel
from docs.models import Doctor


class ExpertDoctorSuggestion(TimeStampedModel):
    doctor = models.ForeignKey(
        Doctor, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.doctor)
