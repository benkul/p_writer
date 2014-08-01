from django import forms
from poetic.models import Poem, Line, SourceText

class PoemForm(forms.ModelForm):
    title = forms.CharField(max_length = 120, initial="untitled")
    author = forms.CharField(max_length = 120, initial="Author")
    num_lines = forms.IntegerField(help_text="Number of lines in poem", initial=4)
    min_lines = forms.IntegerField(help_text="Minimum words per line", initial=3)
    max_lines = forms.IntegerField(help_text="Maximum words per line", initial=6)
    poem_source = forms.ModelChoiceField(queryset=SourceText.objects.all())

    class Meta:
        model = Poem
        fields = ('title', 'author', 'num_lines', 'min_lines', 'max_lines', 'poem_source')
