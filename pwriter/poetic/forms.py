from django import forms
from poetic.models import Poem, Line, SourceText, UserProfile
from django.contrib.auth.models import User

class PoemForm(forms.ModelForm):
    title = forms.CharField(max_length = 120, initial="untitled")
    num_lines = forms.IntegerField(help_text="Number of lines in poem", initial=4)
    min_lines = forms.IntegerField(help_text="Minimum words per line", initial=3)
    max_lines = forms.IntegerField(help_text="Maximum words per line", initial=6)
    poem_source = forms.ModelChoiceField(queryset=SourceText.objects.all())


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