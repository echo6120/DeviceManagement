from django import forms

from DeviceManagement.models import DeviceSystem,Device


class DeviceSystemForm(forms.ModelForm):
    devicesystem = forms.CharField(label="devicesystem")
    class Meta:
        model = DeviceSystem
        fields = ("System",)

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ("device_name","owner","borrow")