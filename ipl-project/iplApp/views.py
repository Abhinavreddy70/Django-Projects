from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import franchise,Player,stadium
from .forms import PlayerForm,stadiumForm,UserRegisterForm,ProfileForm
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
                      
                      #franchise views

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
    Franchise = franchise.objects.get(id=id)
    return render(request,'franchise_details.html',{'franchise':Franchise})

def update_franchise(request,id):
    Franchise=franchise.objects.get(id=id)
    if request.method=='POST':
        Franchise.name=request.POST.get('name')
        Franchise.short_name=request.POST.get('short_name')
        Franchise.founded_year=request.POST.get('founded_year')
        Franchise.no_of_trophies=request.POST.get('no_of_trophies')
        Franchise.city=request.POST.get('city')
        Franchise.owner=request.POST.get('owner') 
        Franchise.coach=request.POST.get('coach')  
        logo=request.FILES.get('logo')

        if request.FILES.get('logo'):
           Franchise.logo=request.FILES.get('logo')
        Franchise.save()
        return redirect('franchise_list')
    else:
        return render(request,'update_franchise.html',{'franchise':Franchise})    
    
def delete_franchise(request,id):
    Franchise=franchise.objects.get(id=id)

    if request.method=='POST':
      Franchise.delete()
      return redirect('franchise_list')
    
                        
                        #player views

def register_player(request):
   if request.method=='POST':
       form=PlayerForm(request.POST,request.FILES)
       if form.is_valid():
             form.save()
             return redirect('player_list')
       else:
             return HttpResponse("Invalid form data",status=400)
   else:
        form=PlayerForm()
        return render(request,'register_player.html',{'form':form})
   

def player_list(request):
    players=Player.objects.all()  
    return render(request,'player_list.html',{'players':players})


def update_player(request,id):
    player=Player.objects.get(id=id)
    if request.method=='POST':
        form=PlayerForm(request.POST,request.FILES,instance=player)
        if form.is_valid():
             form.save()
             return redirect('player_list')
        else:
             return HttpResponse("Invalid form data",status=400)
    else:
        form=PlayerForm(instance=player)
        return render(request,'update_player.html',{'form':form})


def delete_player(request,id):
    player=Player.objects.get(id=id)

    if request.method=='POST':
      player.delete()
      return HttpResponse('Player deleted successfully')


                       #stadium views
def register_stadium(request):
    if request.method=='POST':
        form=stadiumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stadium_list')
            print()
    else:  
        form=stadiumForm()
    return render(request,'register_stadium.html',{'form':form})

def stadium_list(request):
    stadiums=stadium.objects.all()  
    return render(request,'stadium_list.html',{'stadiums':stadiums})


def update_stadium(request,id):
    Stadium=stadium.objects.get(id=id)
    if request.method=='POST':
        form=stadiumForm(request.POST,instance=Stadium)
        if form.is_valid():
             form.save()
             return redirect('stadium_list')
        else:
             return HttpResponse("Invalid form data",status=400)
    else:
        form=stadiumForm(instance=Stadium)
        return render(request,'update_stadium.html',{'form':form})


def delete_stadium(request,id):
    Stadium=stadium.objects.get(id=id)

    if request.method=="POST":
        Stadium.delete()
    return redirect('stadium_list')

                  #user registration view
def register_user(request):
    if request.method=="POST":
         user_form=UserRegisterForm(request.POST)
         profile_form=ProfileForm(request.POST,request.FILES)
         if user_form.is_valid() and profile_form.is_valid():
            #creation of user
            user=user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            #creation of profile
            Profile=profile_form.save(commit=False)
            Profile.user=user
            Profile.save()
            return HttpResponse("your account has been created successfully! you can now login")
    else:
        user_form=UserRegisterForm()
        profile_form=ProfileForm()
        return render(request,'register_user.html',{'user_form':user_form,'profile_form':profile_form})

    


