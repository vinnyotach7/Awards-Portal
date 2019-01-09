from django import forms
from .models import Project, Profile, Reviews, Votes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile', 'posted_time', 'user']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude = ['project', 'user']
        fields = ['comment']


class EditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']


rating_choices = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]


class Votess(forms.Form):
    design = forms.CharField(label='Design level',
                             widget=forms.RadioSelect(choices=rating_choices))

    usability = forms.CharField(
        label='Usability level', widget=forms.RadioSelect(choices=rating_choices))

    creativity = forms.CharField(
        label='Creativity level', widget=forms.RadioSelect(choices=rating_choices))

    content = forms.CharField(label='Content level',
                              widget=forms.RadioSelect(choices=rating_choices))
