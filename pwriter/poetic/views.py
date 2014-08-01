#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from poetic.models import Poem, Line



def index(request):
    context = RequestContext(request)
    devil_haircut = Poem.
    return render_to_response('poetic/index.html', context)

