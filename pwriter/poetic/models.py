from django.db import models
from random import randrange


# Create your models here.
class Poem(models.Model):
    num_lines = models.IntegerField(default=randrange(3, 7))
    num_words_per_line = models.IntegerField(default=randrange(4, 8))


