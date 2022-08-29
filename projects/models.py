from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = _('Category')
        verbose_name_plural = _('Categorys')


# this class is an auxiliary class for status attribue in 'Project' model
class ProjectStatus(models.IntegerChoices):
    # -the name of attribute we will use it in the code
    # -the number we will use it in the database
    # -the string we will display it to the user
    PENDING = 1, _('Pending')
    COMPLETED = 2, _('Completed')
    POSTPONED = 3, _('Postponed')
    CANCELED = 4, _('Canceld')

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=ProjectStatus.choices, default=ProjectStatus.PENDING)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # the model AUTH_USER_MODEL is exist by default in django
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta: 
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
    