import django_filters
from .models import Doctor


class DoctorFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Doctor
        fields = ['city_location']
