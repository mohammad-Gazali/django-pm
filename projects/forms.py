from django import forms
from .models import Project, Task, Category
from django.utils.translation import gettext as _

attrs = {'class': 'form-control'}

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category','title', 'description']
        labels = {
            'category': _('Category'),
            'title': _('Title'),
            'description': _('Description')
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs)
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'status']
        labels = {
            'category': _('Category'),
            'title': _('Title'),
            'status': _('Status')
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'status': forms.Select(attrs=attrs)
        }