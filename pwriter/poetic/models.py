from django.db import models
from random import randrange
from poetic_bits import Markov, Poem_Attributes
from textblob import Textblob
import nltk


# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=120)
    num_lines = models.IntegerField(default=randrange(3, 7))
    num_words_per_line = models.IntegerField(default=randrange(4, 8))
    author = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title

    def poem_stats(self):
        return "number of lines: %r  number of words per line: %r" % (self.num_lines, self.num_words_per_line)

    def return_poem(self):
        byline = "%s by %s\n" % (self.title, self.author)
        current_poem = []
        poetry = ""
        for line in current_poem:
            poetry += line + "\n"

        return byline + "\n" + poetry






class Line(models.Model):
    poem_part = models.ForeignKey(Poem)
    poem_line = models.CharField(max_length=200)
    line_number = models.IntegerField()
    title = models.CharField(default=Poem.title)

    def __unicode__(self):
        return self.poem_line

    def line_num_line(self):
        line = {self.line_number : self.poem_line}
        return line

    def poem_line_list(self, inpug):
        poem_list = self.objects.get(inpug=self.poem_part, order_by='line_number')
        return poem_list


