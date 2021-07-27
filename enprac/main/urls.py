from django.urls import path
from main.views import about, home

urlpatterns = [
    path('home', home),
    path('about', about)
]