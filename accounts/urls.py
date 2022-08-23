from django.urls import path, include
from django.contrib.auth.views import LoginView
from accounts.forms import UserLoginForm

# ### {IMPORTANT}: YOU SHOULD PUT THE 'path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login')' BEFORE  'path('', include('django.contrib.auth.urls'))' ###
urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),  # this class is built-in class in django, this class need an input inside as_view(authentication_form=...) where this input is the our form in forms.py in accounts folder
    path('', include('django.contrib.auth.urls'))  # this url is built-in url in django
]
