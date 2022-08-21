from django import forms
from .models import Project, Task, Category


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'category': forms.Select()
        }