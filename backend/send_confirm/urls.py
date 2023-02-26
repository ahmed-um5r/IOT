from django.contrib import admin
from django.urls import path, include 
from . import views 
from .views import create_post, submit_email

 

urlpatterns = [
    path('post/create/', create_post, name='create_post'),
    path('submit_email/', submit_email, name='submit_email'),
]

