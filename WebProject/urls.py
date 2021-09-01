"""WebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WebApp import views 
#from BootApp import views

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', views.home_Page,name ="home_page"), 
    path( 'registrationpage/' , views.registration_Page),
    path('loginpage/',views.login_Page),
    path('logoutpage/',views.logout_Page),

    path('indexpage/', views.index_page), 

    path('registrationssuccess/',views.registration_success_Page),
    path('loginsuccess/',views.login_success_Page),
    path('logoutsuccess/',views.logout_success_Page),
    #path('bootapp/',views.bootfun),

	# add apis urls
	path('api', include("api.urls"))



    
]
