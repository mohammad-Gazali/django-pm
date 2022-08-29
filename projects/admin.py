from django.contrib import admin
from .models import Project, Task, Category

# Register your models here.


# we can display models inside control panel like this:
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Task)
