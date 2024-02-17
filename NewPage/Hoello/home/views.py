from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
      name= request.POST.get('name')
      email= request.POST.get('email')
      password = request.POST.get('password')
      my_user=User.objects.create_user(name,email,password)
      my_user.save()
      
    
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
       email = request.POST.get('email')
       password = request.POST.get('password')
       user=authenticate(request,Email=email,Password=password)
       
       if user is not None:
           login(request, user)
           return redirect ('home.html')
       else:
           return HttpResponse("id password is not match!!!")
       
    return render(request, 'login.html')

def home(request):
    
    return render(request, 'home.html')

def logoutpage(request):
    
    return render(request, 'login.html')