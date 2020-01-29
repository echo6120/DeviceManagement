from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from DeviceManagement.forms import DeviceSystemForm, DeviceForm
from DeviceManagement.models import DeviceSystem, Device


@csrf_exempt
def device_system(request):
    if request.method == "GET":
        #获取全部系统
        systems = DeviceSystem.objects.all()
        system_form = DeviceSystemForm()
        return render(request, "device/device_system.html", {"systems": systems, 'system_form': system_form})
    if request.method == "POST":
        system_name = request.POST['system_name']
        systems = DeviceSystem.objects.filter(System=system_name)
        if systems:
            return HttpResponse('2')
        else:
            DeviceSystem.objects.create(System=system_name)
            return HttpResponse("1")

@csrf_exempt
def device_post(request):
    if request.method == "GET":
        #获取全部设备
        devices = Device.objects.all()
        device_form = DeviceForm()
        systems = DeviceSystem.objects.all()
        return render(request, "device/device.html", {"devices": devices, 'device_form': device_form,"systems":systems})
    if request.method == "POST":
        device_name = request.POST['device_name']
        owner = request.POST['owner']
        borrow = request.POST['borrow']
        system = DeviceSystem.objects.get(id=request.POST["system_id"])
        device = Device.objects.filter(device_name=device_name)
        if device:
            return HttpResponse('2')
        else:
            Device.objects.create(device_system=system,device_name=device_name,owner=owner,borrow=borrow)
            return HttpResponse("1")


@require_POST
@csrf_exempt
def rename_device_system(request):
    device_system_name = request.POST["system_name"]
    device_system_id = request.POST['device_system_id']
    try:
        line = DeviceSystem.objects.get(id=device_system_id)
        line.System = device_system_name
        line.save()
        return HttpResponse("1")
    except:
        print("888")
        return HttpResponse("0")

@require_POST
@csrf_exempt
def rename_device_borrow(request):
    device_borrow = request.POST["borrow"]
    device_id = request.POST['device_id']
    try:
        line = Device.objects.get(id=device_id)
        line.borrow = device_borrow
        line.save()
        return HttpResponse("1")
    except:
        print("888")
        return HttpResponse("0")


@require_POST
@csrf_exempt
def del_device_system(request):
    device_system_id = request.POST["device_system_id"]
    try:
        line = DeviceSystem.objects.get(id=device_system_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

