from django.contrib import admin
from .models import Project, Task, Category
from django.db.models import Count

# Register your models here.

# ### this section was commented because of using classes and decorators below instead of using admin.site.register() ###
# we can display models inside control panel like this:
# admin.site.register(Category)
# admin.site.register(Project)
# admin.site.register(Task)



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # this attribute has a list that contains all the columns which we want to add inside main tabel of Project model inside control panel
    # we can add a new column into table by adding it to this list, but we should def a function inside this class that has the same name of this new column
    list_display = ['title', 'status', 'user', 'category', 'created_at', 'task_count']

    # this attribute determines the number of element inside one page
    list_per_page = 20

    # this attribute has a list that contains the columns that we can edit from the table
    list_editable = ['status']

    # this attribute determines related models ( like select_related() and prefetch_related() functions )
    list_select_related = ['category', 'user']


    # this function should has the same name of the new column which we add in list_display
    # but if we use 'return obj.task_set.count()' then we will face the query huge number another time
    # so if we want to solve this we should define a new function inside the class that is called get_queryset(self, requset)
    def task_count(self, obj):
        # return obj.task_set.count()  # [Note: notice that the parameter obj here refers to Project object]
        return obj.task_count  # we use this return because of using get_queryset() function below, and this is the reason of commenting the previous return

    def get_queryset(self, request):
        query_set =  super().get_queryset(request)
        query_set = query_set.annotate(task_count=Count('task'))  # we use annotate() function to add a new select relation inside annotate() function, in the inputs of this function we add a key arguments where the key is the name of column in list_display and the value is the function we want to apply, notice that we import Count() function for counting the tasks of Project object
        return query_set


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_editable = ['is_completed']
    list_per_page = 20
    list_select_related = ['project']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20