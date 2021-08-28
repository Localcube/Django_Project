from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import RegistrationModelForm

def home_Page(request): 
	return render(request, "home_page.html")

def registration_Page(request):
    	
     if request.method == "POST":  
        form = RegistrationModelForm(request.POST)  
        if form.is_valid():  
           form.save(commit=True) 
        return HttpResponseRedirect('/registrationssuccess')  
            
     else:  
         
        form = RegistrationModelForm()  
     return render(request,'registration_page.html',{'form':form})  

def login_Page(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('/'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
   else:
        return render(request, 'WebApp/login_page.html', {})

def logout_Page(request):
       return render(request, "logout_page.html")

def index_page(request):  
    return render(request,'index_page.html')   

def registration_success_Page(request):
       return render(request, 'registration_success.html')

def login_success_Page(request):
       return render(request, 'login_success.html')

def logout_success_Page(request):
       return render(request, 'logout_success.html')





