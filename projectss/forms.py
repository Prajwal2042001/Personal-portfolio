from django import forms
from projectss.models import Project_list

class projectform(forms.ModelForm):
    class Meta:
        model=Project_list
        fields='__all__'