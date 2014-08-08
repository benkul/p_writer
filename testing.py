import nltk
import random
from textblob import TextBlob
import re


class Markov(object):

  def __init__(self, open_file):
    self.cache = {}
    self.open_file = open_file
    self.words = self.file_to_words()
    self.word_size = len(self.words)
    self.database()


  def file_to_words(self):
    self.open_file.seek(0)
    data = self.open_file.read()
    words = data.split()
    return words


  def triples(self):
    """ Generates triples from the given data string. So if our string were
	"What a lovely day", we'd generate (What, a, lovely) and then
	(a, lovely, day).
    """

    if len(self.words) < 3:
      return

    for i in range(len(self.words) - 2):
      yield (self.words[i], self.words[i+1], self.words[i+2])

  def database(self):
    for w1, w2, w3 in self.triples():
      key = (w1, w2)
      if key in self.cache:
		self.cache[key].append(w3)
      else:
		self.cache[key] = [w3]

  def generate_markov_text(self, size):
	seed = random.randint(0, self.word_size-3)
	seed_word, next_word = self.words[seed], self.words[seed+1]
	w1, w2 = seed_word, next_word
	gen_words = []
	for i in xrange(size):
	  gen_words.append(w1)
	  w1, w2 = w2, random.choice(self.cache[(w1, w2)])
	gen_words.append(w2)
	return ' '.join(gen_words)

file = open('forestry6.txt', 'r')
poem_gen = Markov(file)

n=1
poem_dict = {}
language_options = ['bg', 'da', 'eo', 'fr', 'de', 'el', 'is', 'ga', 'it', 'ja', 'es']
language_choice = random.choice(language_options)
# for item in range(20):
	# #id = Poem.pk
	# #print poem_gen
	# #line = "hippos shit all over the palace"
	# line = poem_gen.generate_markov_text(random.randrange(3,9))
	# line = TextBlob(line)
	# # line = line.translate(to=random.choice(language_options))
	# # line = line.translate(to=random.choice(language_options))
	
	# # #print language_choice
	# # line = line.translate(to=random.choice(language_options))
	# # line = line.translate(to='en')
	# line = str(line)
	# if line.find('the', (len(line) - 3), len(line)) == (len(line) - 3):
		# line += " %s" % poem_gen.generate_markov_text(0)
	# if line.find('and', (len(line) - 3), len(line)) == (len(line) - 3):
		# line += " %s" % poem_gen.generate_markov_text(0)
	# print line
	# #Line.create(poem_part=id, poem_line=line, line_number=n)
	# n += 1

def poem_maker(lines, min_word, max_word):
	n=1
	line_list = []
	for line in range(lines):
		words_in_line = random.randrange(min_word, max_word)
		line = poem_gen.generate_markov_text(words_in_line)
		line_list.append( [n, words_in_line, line] )
		n += 1
	print line_list	
	#generate all poem lines
	line_string = ""
	# convert to string for translation
	for item in line_list:
		line_string += str(item[2] + " ")
	line_string = TextBlob(line_string)
	line_string = line_string.translate(to='ja')
	line_string = line_string.translate(to='en')
	line_string = unicode(line_string)
	#break back into lines
	word_list = re.sub("[^\w]", " ", line_string).split()
	#print "list of words: %s" % word_list
	for line in line_list:
		x = 0
		temp_list = []
		temp = ""
		while x <= (line[1]):
			try:
				temp_list.append(word_list.pop(0))
				
			except IndexError:
				x = line[1]
			x += 1
		#temp_list = word_list.slice([0,(line[1] or -1)])
		for item in temp_list:
			temp += "%s " % item
		line[2] = temp
		#final = Line.objects.create_line(id, line_list[2], line_list[0])
		print line[2]

		
poem_maker(3, 4, 7)