from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index, name= 'home'),
    path("about",views.about, name= 'aboutme'),
    path("service",views.service, name= 'servcies'),
    path("contact",views.contact, name= 'contact'),
    
]