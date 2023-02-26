
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post2
import random 
from django.utils import timezone
import datetime
import time
from datetime import timedelta
#from .forms import PostForm 



def submit_email(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        x=datetime.datetime.now()
#        raise Exception(x)
        Post2.objects.create(title = title, content=content, pub_date=x) 


def create_post(request):
    post_list = Post2.objects.all() 
    return render(request, 'create_post.html',{"post_list":post_list})

 