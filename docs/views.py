from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from docs.models import CityLocation
from .models import Doctor
from .forms import RecordForm
from .filters import DoctorFilter


def product(request):
    return render(request, "docs/product.html")


def service_index(request):
    filter = DoctorFilter(request.GET, queryset=Doctor.objects.all())
    city_locations = CityLocation.objects.all()
    context = {
        "doctors": filter.qs[:10],
        "filter": filter,
        "city_locations": city_locations,
    }
    return render(request,  "docs/service.html", context=context)


@login_required
def appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            appointment_obj = form.save(commit=False)
            appointment_obj.user = request.user
            appointment_obj.save()
            return redirect('authentication:profile')
    else:
        form = RecordForm(
            initial={'doctor': doctor, 'email': request.user.email})
    context = {
        "doctor": doctor,
        "form": form,
    }
    return render(request, "docs/appointment.html", context=context)
