from django import forms
from poetic.models import Poem, Line

class PoemForm(forms.ModelForm):
    title = forms.CharField(max_length = 120, help_text="Title", initial="untitled")
    author = forms.CharField(max_length = 120, help_text="Author")
    num_lines = forms.IntegerField(help_text="Number of lines in poem")
    min_lines = forms.IntegerField(help_text="Minimum words per line")
    max_lines = forms.IntegerField(help_text="Maximum words per line")


    class Meta:
        model = Poem
        fields = ()
