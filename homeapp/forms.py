from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username',max_length=30)
    
    class Meta:
        model= User
        Fields = ['username', 'password1', 'password2']
        
