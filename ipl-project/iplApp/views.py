from django.shortcuts import render
from django.http import HttpResponse
from .models import franchise
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
    

def register_franchise(request):

    if request.method=='POST':
        name=request.POST.get('name')
        short_name=request.POST.get('short_name')
        founded_year=request.POST.get('founded_year')
        no_of_trophies=request.POST.get('no_of_trophies')
        city=request.POST.get('city')
        owner=request.POST.get('owner') 
        coach=request.POST.get('coach')  
        logo=request.FILES.get('logo')

                                     
        franchise.objects.create(
            name=name,
            short_name=short_name,
            founded_year=founded_year,
            no_of_trophies=no_of_trophies,
            city=city,
            owner=owner,
            coach=coach,
            logo=logo,
        )
        return HttpResponse("Franchise registered successfully")
    else:
     return render(request,'register_franchise.html')
    
def franchise_list(request):
    franchises=franchise.objects.all()  
    return render(request,'franchise_list.html',{'franchises':franchises})


def franchise_details(request,id):
    print('franchise id:',id)
    Franchise = franchise.objects.get(id=id)
    return render(request,'franchise_details.html',{'franchise':Franchise})