from django.shortcuts import render, redirect
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm, ProfileForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    
    def get_success_url(self):
        login(self.request, self.object)
        return reverse_lazy('Project_list')


# this function is for changing the profile of the user
@login_required  # this decorator means that this function is only available if the user is login, so when the user is not login this decorator will redirect to login page
def edit_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})
