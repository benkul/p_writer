#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from poetic.models import Poem, Line
from poetic.forms import PoemForm


def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PoemForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = PoemForm()

    return render_to_response('poetic/index.html', {'form': form}, context)





