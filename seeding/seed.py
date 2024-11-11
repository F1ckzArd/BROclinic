import random
from django.utils import timezone
from docs.models import Doctor, CityLocation
from main.models import ExpertDoctorSuggestion
from django.contrib.auth import get_user_model

User = get_user_model()


def seed():
    user = User.objects.create(
        username="admin",
        email="admin@example.com",
        is_superuser=True,
        is_staff=True
    )
    user.set_password("admin.password@1234",)
    user.save()

    CityLocation.objects.create(name="Astana")
    CityLocation.objects.create(name="Aktobe")
    c = CityLocation.objects.create(name="Barmagatai")

    for i in range(3):
        user = User.objects.create(
            username=f"user{i}",
            email=f"user{i}@example.com",
            city_location=c
        )
        user.set_password("user{i}.password@1234",)
        user.save()

    for i in range(5, 11):
        user = User.objects.create(
            username=f"user{i}",
            email=f"user{i}@example.com",
        )
        user.set_password("user{i}.password@1234",)
        user.save()
        Doctor.objects.create(
            user=user,
            institute="Instiyure random",
            description="sevbewvg vweuivwe vewjvber dv vdv vreverver vreverv ververv vrever",
            city_location=c
        )

    doctors = Doctor.objects.all()
    for doc in doctors:
        ExpertDoctorSuggestion.objects.create(
            doctor=doc
        )
