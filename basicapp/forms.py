from django import forms
from django.core.mail import EmailMessage
from django.forms import fields, widgets
from numpy import require
from .models import Share

class CreateForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ('day', 'content')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


# 後で作成 with菊池
# class SelectPortForm(forms.Form):
#     answers = forms.fields.ChoiceField(
#         ports = (
#             "千葉港",
#             "東京港",
#             "川崎港",
#             "横浜港",
#             "横須賀港",
#             "木更津港"
#         ),
#     required=True,
#     widget=forms.widgets.Select()
#     )