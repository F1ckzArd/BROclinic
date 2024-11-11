from django.db import models
from utils.models import TimeStampedModel
from django.contrib.auth import get_user_model
from authentication.models import CityLocation

User = get_user_model()


class Doctor(TimeStampedModel):
    description = models.TextField(
        blank=True, null=True, verbose_name="Description")
    user = models.OneToOneField(
        User, null=False, blank=False, on_delete=models.CASCADE)
    institute = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Institute"
    )
    face_image = models.ImageField(upload_to='doctors')
    city_location = models.ForeignKey(
        CityLocation, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.user)


class Category(TimeStampedModel):
    name = models.CharField(max_length=150, unique=True, verbose_name="Name")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(TimeStampedModel):
    name = models.CharField(max_length=150, unique=True, verbose_name="Name")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Description")
    image = models.ImageField(
        blank=True, null=True, upload_to="docs_images", verbose_name="Image"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Price"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Discount"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Category"
    )

    def __str__(self):
        return f"{self.name} Quantity - {self.quantity}"


class RecordStatus(models.TextChoices):
    PLANNED = 'planned', 'Planned'
    DONE = 'done', 'Done'
    ABSENT = 'absent', 'Absent'


class RecordApprovalStatus(models.TextChoices):
    WAITING = 'waiting', 'Waiting for Approval'
    APPROVED = 'approved', 'Approved'
    REJECTED = 'rejected', 'Rejected'


class Record(TimeStampedModel):
    first_name = models.CharField(max_length=150, verbose_name="First Name")
    last_name = models.CharField(max_length=150, verbose_name="Last Name")
    email = models.EmailField(
        max_length=200, blank=False, null=False, verbose_name="Email"
    )
    question = models.TextField(
        blank=False, null=False, verbose_name="Question")
    phone = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Phone number"
    )
    doctor = models.ForeignKey(
        Doctor, null=False, blank=False, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10, choices=RecordStatus.choices, default=RecordStatus.PLANNED)
    approval_status = models.CharField(
        max_length=10, choices=RecordApprovalStatus.choices, default=RecordApprovalStatus.WAITING)
