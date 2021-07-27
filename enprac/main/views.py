from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="http://localhost:8000")
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'extensions/about.html')