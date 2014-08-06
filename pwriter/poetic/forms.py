from django import forms
from poetic.models import Poem, Line, SourceText, UserProfile
from django.contrib.auth.models import User
from random import randrange

class PoemForm(forms.ModelForm):
    title = forms.CharField(max_length = 120, help_text="Title (must be unique value)", initial="untitled")
    num_lines = forms.IntegerField(help_text="Number of lines in poem", initial=randrange(4,8))
    min_lines = forms.IntegerField(help_text="Minimum words per line", initial=randrange(3, 5))
    max_lines = forms.IntegerField(help_text="Maximum words per line", initial=randrange(6, 9))
    poem_source = forms.ModelChoiceField(queryset=SourceText.objects.all(), help_text="Source text for poem generation")


    class Meta:
        model = Poem
        fields = ('title', 'num_lines', 'min_lines', 'max_lines', 'poem_source')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')