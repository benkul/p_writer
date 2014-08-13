from random import randrange, choice
from django import forms
from poetic.models import Poem, Line, SourceText, UserProfile
from django.contrib.auth.models import User


class PoemForm(forms.ModelForm):
    title = forms.CharField(max_length = 120, help_text="Title (must be unique value)", initial='untitled')
    num_lines = forms.ChoiceField(help_text="Number of lines in poem", initial=3, choices=[(x, x) for x in range(2, 10)])
    min_lines = forms.ChoiceField(help_text="Minimum words per line", initial=randrange(3, 5), choices=[(x, x) for x in range(2, 6)])
    max_lines = forms.ChoiceField(help_text="Maximum words per line", initial=randrange(6, 10), choices=[(x, x) for x in range(5, 11)])
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

class LineEditForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = ('poem_line',)