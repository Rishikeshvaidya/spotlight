from django import forms
from Home.models import notification


class notificationform(forms.ModelForm):
    class Meta:
        model =notification
        fields=['adminnotice']