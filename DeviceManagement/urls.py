from django.urls import path, re_path

from . import views

app_name = "DeviceManagement"
urlpatterns =[
    path('device-system/',views.device_system,name="device_system"),
    path('rename-device-system/',views.rename_device_system,name="rename_device_system"),
    path('del-device-system/',views.del_device_system,name="del_device_system"),

    path('add-device/',views.device_post,name="add_device"),
    path('rename-device/',views.rename_device_borrow,name="rename_device_borrow"),


]