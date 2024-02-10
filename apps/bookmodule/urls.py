
#we dont need to import admin
from django.urls import path
from django.urls import include
from apps.bookmodule import views

urlpatterns = [
    path('',views.index,name='index'),
    
]

