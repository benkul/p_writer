from django.db import models
from random import randrange




# Create your models here.
class SourceText(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=400) # short description of types of imagary in class

    def __unicode__(self):
        return self.name

    def get_description(self):
        return "%s: %s" % (self.name, self.description)


class Poem(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    num_lines = models.IntegerField(default=randrange(3, 7))
    min_words = models.IntegerField(default=3)
    max_words = models.IntegerField(default=randrange(5, 8))
    poem_source = models.ForeignKey(SourceText)

    def __unicode__(self):
        return self.title






class Line(models.Model):
    poem_part = models.ForeignKey(Poem)
    poem_line = models.CharField(max_length=200)
    line_number = models.IntegerField()


    def __unicode__(self):
        return self.poem_line

    def line_num_line(self):
        line = {self.line_number : self.poem_line}
        return line




