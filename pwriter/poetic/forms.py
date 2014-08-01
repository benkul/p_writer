from django import forms
from poetic.models import Poem, Line

class PoemForm(forms.ModelForm):


    class Meta:
        model = Poem
