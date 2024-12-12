from django.shortcuts import render,HttpResponse
from projectss.models import Project_list
from projectss.forms import projectform
from app.models import Registered_list

def insert(request):
    ins=projectform()
    if request.method=="POST" and request.FILES:
        frm=projectform(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return HttpResponse("Data Stored in table")
    return render(request,'ins.html',{'form':ins})

def read(request):
    a=Project_list.objects.all()
    return render(request,'projects.html',{'read':a})

def delete(request,a):
    Project_list.objects.filter(id=a).delete()
    return HttpResponse("Deleted Successfully")

def update(request,praju):
    z=Project_list.objects.get(id=praju)
    var=projectform(instance=z)
    if request.method=="POST" and request.FILES:
        z=projectform(request.POST,request.FILES,instance=z)
        if z.is_valid():
            z.save()
            return HttpResponse("Data Updated in table")
    return render(request,'ins.html',{'form':var})
