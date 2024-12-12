from django import forms
from app.models import Registered_list

class registerform(forms.ModelForm):
    class Meta:
        model=Registered_list
        widgets={'password':forms.PasswordInput()}
        widgets={'confirm_password':forms.PasswordInput()}
        fields='__all__'