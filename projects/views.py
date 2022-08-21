from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Project, Task, Category
from .forms import ProjectCreateForm

# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectCreateForm
    success_url = reverse_lazy('Project_list')
