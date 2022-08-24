from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project, Task, Category
from .forms import ProjectCreateForm, ProjectUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/list.html'
    paginate_by = 6  # this attribute determines the number of this object in one page 

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id': self.request.user}  # the element inside where dictionary means that we should list only the projects for only the user not all projects of all users, so when we determine that the id of user of projects then the projects that will display are only that the user owns [ you understand me :) ]
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectCreateForm
    success_url = reverse_lazy('Project_list')

    # here the function create the project and put the id of user inside database for differentiating between users, so the object project will also include user_id
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectUpdateForm
    
    # this function determines the test we want, if the test successes then we could use ProjectCreatView, but, if the test doesn't success then the class UserPassesTestMixin will prevent creating the project
    def test_func(self):  # this function return boolean, True for successing and  False for failing
        return self.get_object().user_id == self.request.user.id  # get_object() function targets the object which we work on (the project we edit for this class) 
    
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id])  # the word object refers to the same object which we edit 


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_list')

    def test_func(self):
        return self.get_object().user_id == self.request.user.id

class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def test_func(self):
        project_id = self.request.POST.get('project', '')
        return Project.objects.get(pk=project_id).user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['is_completed']
    http_method_names = ['post']

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])
