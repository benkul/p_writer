from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
#from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    return render('generator/index.html', context)

