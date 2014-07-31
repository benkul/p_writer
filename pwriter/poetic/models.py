from django.db import models
from random import randrange


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
        current_poem = Line.poem_line_list(self)
        poetry = ""
        for line in current_poem:
            poetry += line + "\n"

        return byline + "\n" + poetry



class Line(models.Model):
    poem_part = models.ForeignKey(Poem)
    poem_line = models.CharField(max_length=200)
    line_number = models.IntegerField()

    def __unicode__(self):
        return self.poem_line

    def line_num_line(self):
        line = {self.line_number : self.poem_line}
        return line

    def poem_line_list(self, poem_id):
        poem_list = self.objects.get(poem_part=poem_id, order_by='line_number')
        return poem_list


