#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from poetic.models import Poem, Line
from poetic.forms import PoemForm
import nltk
from textblob import TextBlob
import random


#helper fucntion to generate poems
def create_poem(title, author, lines, min_word, max_word, source):
    text = source.objects.get(SourceText.text)


def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=True)
            create_poem(poem.title, poem.author, poem.num_lines, poem.min_words, poem.max_words, poem.source)

            return get_poem(request, poem.author, poem.title)
        else:
            print form.errors
    else:
        form = PoemForm()

    return render_to_response('poetic/index.html', {'form': form}, context)

def get_poem(request, user, title):
    context = RequestContext(request)
    # code to get and return poem
    return render_to_response('poetic/user/title', {'poem': dict}, context)



