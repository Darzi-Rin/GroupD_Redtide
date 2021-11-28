from django import forms
from django.core.mail import EmailMessage
from django.forms import fields
from .models import Share

class CreateForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ('day', 'content')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'