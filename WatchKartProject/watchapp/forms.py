from django import forms
from .models import WatchApp

class WatchAppForm(forms.ModelForm):
    class Meta:
        model = WatchApp
        fields = '__all__'