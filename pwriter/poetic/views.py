import random
import re
import nltk
from textblob import TextBlob
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from poetic.models import Poem, Line, SourceText, UserProfile
from poetic.forms import PoemForm, UserForm, UserProfileForm
from poetic.poetic_bits import Markov
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth import authenticate, login



#random languages translations

#helper fucntion to generate poems
def create_poem(title, author, lines, min_word, max_word, source, pk):
    text = SourceText.objects.get(name=source)
    print text.get_location()

    text = open(text.get_location(), 'r') #TODO: build path to static file
    poem_gen = Markov(text)
    n=1
    poem_dict = {}
    for line in range(lines):
        id = Poem.objects.get(pk=pk)
        line = poem_gen.generate_markov_text(random.randrange(min_word, max_word))
        line = TextBlob(line)
        line = line.translate(to='es')
        line = line.translate(to='en')
        line = line.translate(to='nl')
        line = line.translate(to='en')

        line = unicode(line)
        final = Line.objects.create_line(id, line, n)
        poem_dict[n] = line
        n += 1
    poem_dict['author'] = author
    poem_dict['title'] = title
    poem_dict['number_of_lines'] = lines
    return poem_dict





def index(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=False)

            print "looking for title {}, user {}".format(poem.title, request.user.username)
            existing_poem_list = Poem.objects.filter(title__startswith=poem.title,
                                                     author__user=request.user).order_by('title').values('title')

            print existing_poem_list
            exact_match = False
            max_value = 0
            p = re.compile('(.*)(_)(\d+)$') # returns (title) (_) (number)
            for title_dict in existing_poem_list:
                if title_dict['title'] == poem.title:
                    #poem.title += "_%s" % len(existing_poem_list)
                    exact_match = True
                else:
                    match_object = p.match(title_dict['title'])
                    if match_object and match_object.groups()[0] == poem.title:
                        max_value = max(int(match_object.groups()[2]), max_value)

            if exact_match:
                poem.title += "_%s" % (max_value + 1)

                print "poem title changed to: %s" % poem.title

            poem.title_slug = slugify(poem.title)

            poem.author = UserProfile.objects.get(user=request.user)
            print poem.title
            poem.save()# = form.save()
            print poem
            create_poem(poem.title, poem.author,
                                        poem.num_lines,
                                        poem.min_words,
                                        poem.max_words,
                                        poem.poem_source,
                                        poem.pk)


            return HttpResponseRedirect("/poetic/{}/{}/".format(poem.author, poem.title_slug))
        else:
            print form.errors
    else:
        form = PoemForm()
    return render_to_response('poetic/index.html', {'form': form}, context)


def retrieve_poem(request, username, title_slug):
    context = RequestContext(request)
    author = UserProfile.objects.get(user__username=username)#.pk
    this_poem = get_object_or_404(Poem, author=author, title_slug=title_slug)
    context_dict = { 'poem' : this_poem }
    return render_to_response('poetic/poem.html', context_dict, context)



def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            temp_pword = user.password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            print user.username
            print user.password
            sign_in = authenticate(username=user.username, password=temp_pword)
            print "authenticated", sign_in.is_authenticated
            login(request, sign_in)
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response('poetic/register.html',
        {'user_form' : user_form, 'profile_form' : profile_form, 'registered': registered},
        context)

def user_profile(request, username):
    context = RequestContext(request)
    poems = Poem.objects.filter(author__user__username=username).order_by('title')
    context_dict = { "poems" : poems }
    return render_to_response('poetic/profile.html', context_dict, context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/poetic/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Poetic account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('poetic/login.html', {}, context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    context = RequestContext(request)
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return render_to_response('poetic/logout.html', {}, context)