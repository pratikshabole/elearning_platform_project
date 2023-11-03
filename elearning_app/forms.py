from django import forms
from django.contrib.auth.models import User
from elearning_app.models import user_profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        labels = {
        'password1': 'Password',
        'password2' : 'Confirm Password'
        }

class user_profileForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    instructor = 'Instructor'
    student = 'Student'
    user_types = [
        (instructor, 'Instructor'),
        (student, 'Student')
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model =  user_profile
        fields = ('bio', 'profile_pic', 'user_type')
