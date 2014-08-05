from django.db import models
from random import randrange
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth.models import User



# Create your models here.
class SourceText(models.Model):
    location = models.CharField(max_length=120) # file name
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=400) # short description of types of imagery in class

    def __unicode__(self):
        return self.name

    def get_description(self):
        return "%s: %s" % (self.name, self.description)

    def get_location(self):
        return str(self.location) # returns name with static root added



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank = True)

    def __unicode__(self):
        return self.user.username

    def get_name(self):
        return "%s" % self.user.username


class Poem(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(UserProfile)
    num_lines = models.IntegerField(default=randrange(3, 7))
    min_words = models.IntegerField(default=3)
    max_words = models.IntegerField(default=randrange(5, 8))
    poem_source = models.ForeignKey(SourceText)
    title_slug = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title


class LineManager(models.Manager):
    def create_line(self, poem_part, poem_line, line_number):
        line = self.create(poem_part=poem_part, poem_line=poem_line, line_number=line_number)
        return line


class Line(models.Model):
    poem_part = models.ForeignKey(Poem)
    poem_line = models.CharField(max_length=200)
    line_number = models.IntegerField()

    objects = LineManager()

    def __unicode__(self):
        return self.poem_line

    def line_num_line(self):
        line = {self.line_number : self.poem_line}
        return line



