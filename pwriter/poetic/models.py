from django.db import models
from random import randrange


# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=120)
    num_lines = models.IntegerField(default=randrange(3, 7))
    num_words_per_line = models.IntegerField(default=randrange(4, 8))

    def __unicode__(self):
        return self.title

    def poem_stats(self):
        return "number of lines: %r  number of words per line: %r" % (self.num_lines, self.num_words_per_line)


