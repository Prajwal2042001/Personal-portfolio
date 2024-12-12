from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from app.models import Registered_list
from app.forms import registerform
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

# def projects(request):
#     return render(request,'projects.html')

def contact(request):
    return render(request,'contact.html')

def start(request):
    return render(request,'start.html')


def register(request):
    var=registerform
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password == confirm_password:
            var=registerform(request.POST)
            if var.is_valid():
                a=var.save(commit=False)
                a.password=make_password(a.password)
                a.save()
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exists')
                    return redirect(register)
                else:
                    user=User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name)
                    user.set_password(password)
                    user.save()
                    return redirect('login')
    else:
        return render (request,'register.html',{'var':var})
    
def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('start')
        else:
            return redirect("register")
    else:
        return render(request,"login.html")
    
def logout_user(request):
    auth.logout(request)
    return redirect('home')

# Additional Operations 
def delete(request,a):
    Registered_list.objects.filter(id=a).delete()
    return HttpResponse("Deleted")