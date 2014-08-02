#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from poetic.models import Poem, Line, SourceText
from poetic.forms import PoemForm
from poetic.poetic_bits import Markov
from django.contrib.staticfiles.templatetags.staticfiles import static
import nltk
from textblob import TextBlob
import random


#helper fucntion to generate poems
def create_poem(title, author, lines, min_word, max_word, source):
    text = SourceText.objects.get(name=source)
    print text.get_location()

    text = open(text.get_location(), 'r') #TODO: build path to static file
    poem_gen = Markov(text)
    n=1
    poem_dict = {}
    for line in range(lines):
        id = Poem.pk
        line = poem_gen.generate_markov_text(random.randrange(min_word, max_word))
        line = TextBlob(line)
        line = line.translate(to='es')
        line = line.translate(to='en')
        line = line.translate(to='nl')
        line = line.translate(to='en')
        line = str(line)
        print line
        Line.create(poem_part=id, poem_line=line, line_number=n)
        poem_dict[n] = line
        n += 1
        return poem_dict





def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=True)
            #create_poem(poem.title, poem.author, poem.num_lines, poem.min_words, poem.max_words, poem.poem_source)

            return get_poem(request, poem.author, poem.title,
                            create_poem(poem.title, poem.author, poem.num_lines, poem.min_words, poem.max_words, poem.poem_source))
        else:
            print form.errors
    else:
        form = PoemForm()

    return render_to_response('poetic/index.html', {'form': form}, context)

def get_poem(request, user, title, dict):
    context = RequestContext(request)
    url = 'poetic/' + user + "/" + title + "/"
    # code to get and return poem
    return render_to_response(url, dict, context)



