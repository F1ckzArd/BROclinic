import django_filters
from .models import Doctor


class DoctorFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr='icontains')
    # city_location = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Doctor
        fields = ['city_location']
