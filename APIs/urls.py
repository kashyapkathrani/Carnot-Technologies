from django.urls import path
from . import views

urlpatterns = [
    path('device', views.getAllDevicesData),
    path('device/<int:device_id>', views.getDeviceDataById) #[24809, 25029, 20984, 6888]
]