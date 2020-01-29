from django.conf.urls import url, include

from django.urls import path

urlpatterns = [
    path('device/',include('DeviceManagement.urls',namespace='device'))

]