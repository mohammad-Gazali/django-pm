from django.urls import path, include
from django.contrib.auth.views import LoginView
from accounts.forms import UserLoginForm
from accounts import views

# ### {IMPORTANT}: YOU SHOULD PUT ALL YOUR URLPATTERNS BEFORE  'path('', include('django.contrib.auth.urls'))' ###
urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),  # this class is built-in class in django, this class need an input inside as_view(authentication_form=...) where this input is the our form in forms.py in accounts folder
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.edit_profile, name='profile'),
    path('', include('django.contrib.auth.urls'))  # this url is built-in url in django
]
