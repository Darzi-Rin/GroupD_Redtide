from django.contrib.auth.forms import UserCreationForm

from basicapp.models import CustomUser

class UserCreateForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     #htmlの表示を変更可能にします
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
       model = CustomUser
       fields = ("username", "email","password1", "password2",)