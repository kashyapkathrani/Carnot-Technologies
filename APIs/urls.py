from django.urls import path
from . import views

urlpatterns = [
    path('device/<int:device_id>', views.getDeviceData) #[24809, 25029, 20984, 6888]
]