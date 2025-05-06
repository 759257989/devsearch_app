from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name' 
        }
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        # self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        # self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        # self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})