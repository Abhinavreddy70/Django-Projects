from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the IPL App Home Page!")

def register(request):
    if request.method=='POST':
         username=request.POST.get('username')
         email=request.POST.get('email')
         password=request.POST.get('password')
         confirm_password=request.POST.get('confirm_password')

         print(username, email,password,confirm_password)
         return HttpResponse("Registration successful")
    else:    
        return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST.get('username') 
        password=request.POST.get('password')
        print(username,password)
        return HttpResponse("Login successful")

    else:
        return render(request,'login.html')       