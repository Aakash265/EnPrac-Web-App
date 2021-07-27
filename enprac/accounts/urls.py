from django.urls import path
from accounts.views import logoutUser, registerPage, loginPage

urlpatterns= [
    path('register', registerPage),
    path('', loginPage),
    path('logout', logoutUser),
]