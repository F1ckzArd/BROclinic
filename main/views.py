from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first
from .models import ExpertDoctorSuggestion

# Create your views here.


def index(request):
    context = {
        'experts': ExpertDoctorSuggestion.objects.order_by('-id')[:4]
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'content': "",
        'text_on_page': "Text"
    }
    return render(request, 'main/about.html', context)
