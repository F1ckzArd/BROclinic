from django.urls import path
from docs import views

app_name = 'docs'

urlpatterns = [
    path('service/', views.service_index, name='index'),
    path('service/appointment/<int:doctor_id>/',
         views.appointment, name='appointment'),
    path('service/product/', views.product, name='product'),
]
