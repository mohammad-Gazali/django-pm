from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project, Task, Category
from .forms import ProjectCreateForm, ProjectUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/list.html'
    paginate_by = 6  # this attribute determines the number of this object in one page 

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectCreateForm
    success_url = reverse_lazy('Project_list')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectUpdateForm
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id])  # the word object refers to the same object which we edit 


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_list')

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])
