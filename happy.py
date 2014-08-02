import nltk
import random
from textblob import TextBlob

file = open('forestry.txt', 'r')

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
	seed = 1 #random.randint(0, self.word_size-3)
	seed_word, next_word = self.words[seed], self.words[seed+1]
	w1, w2 = seed_word, next_word
	gen_words = []
	for i in xrange(size):
	  gen_words.append(w1)
	  w1, w2 = w2, random.choice(self.cache[(w1, w2)])
	gen_words.append(w2)
	return ' '.join(gen_words)
	
Tweet = Markov(file)
listemp = []
novel = open('poetry3.txt', 'a')
options = [0, 2, 4, 6, 8]
odd_options = [-1, 1, 2, 3, 5, 7]

def double_remover(line):
	list = line.split(' ')
	listmp = list
	for item in range(len(list)-1):
		if list[item] == list[item + 1]:
			list.pop(item + 1)
	line = ''.join(list)
	return line

def filter_insignificant(chunk, tag_suffixes=['DT', 'CC']):
  good = []

  for word, tag in chunk:
    ok = True

    for suffix in tag_suffixes:
      if tag.endswith(suffix):
        ok = False
        break

    if ok:
      good.append((word, tag))

  return good
  
def first_chunk_index(chunk, pred, start=0, step=1):
  l = len(chunk)
  end = l if step > 0 else -1

  for i in range(start, end, step):
    if pred(chunk[i]):
      return i

  return None

plural_verb_forms = {
  ('is', 'VBZ'): ('are', 'VBP'),
  ('was', 'VBD'): ('were', 'VBD')
}

singular_verb_forms = {
  ('are', 'VBP'): ('is', 'VBZ'),
  ('were', 'VBD'): ('was', 'VBD')
}
  
def correct_verbs(chunk):
  vbidx = first_chunk_index(chunk, lambda (word, tag): tag.
startswith('VB'))
  # if no verb found, do nothing
  if vbidx is None:
    return chunk

  verb, vbtag = chunk[vbidx]
  nnpred = lambda (word, tag): tag.startswith('NN')
  # find nearest noun to the right of verb
  nnidx = first_chunk_index(chunk, nnpred, start=vbidx+1)
  # if no noun found to right, look to the left
  if nnidx is None:
    nnidx = first_chunk_index(chunk, nnpred, start=vbidx-1, step=-1)
  # if no noun found, do nothing
  if nnidx is None:
    return chunk

  noun, nntag = chunk[nnidx]
  # get correct verb form and insert into chunk
  if nntag.endswith('S'):
    chunk[vbidx] = plural_verb_forms.get((verb, vbtag), (verb, vbtag))
  else:
    chunk[vbidx] = singular_verb_forms.get((verb, vbtag), (verb,
vbtag))

  return chunk  

for x in range(10):
	line1 = Tweet.generate_markov_text(8)
	blob1 = TextBlob(line1)
	blob1 = blob1.translate(to='es')
	blob1 = blob1.translate(to='en')
	blob1 = blob1.translate(to='nl')
	blob1 = blob1.translate(to='en')

	
	blob1 = str(blob1)
	print blob1



file.close()	


