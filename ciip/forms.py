from models import UserProfile
from django.forms import ModelForm
#from django.contrib.auth.models import User
class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name', 'email', 'password','university')
