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
	line2 =  Tweet.generate_markov_text(8)
	line3 = Tweet.generate_markov_text(6)
	#double_remover(line1)
	#double_remover(line2)
	#double_remover(line3)
	the = "the"
	india = "in"
	so = "so"
	of = "of"
	either = "or"
	plus = "and"
	replacement = [" light", " dark", " end", " moon", " owl", " wolf"]
	if line1.find(the, (len(line1) - 3), len(line1)) == (len(line1) - 3):
		line1 += random.choice(replacement)
	elif line1.find(india, (len(line1) - 2), len(line1)) == (len(line1) - 2):
		line1 += (" death")
	elif line1.find(so, (len(line1) - 5), len(line1)) == (len(line1) - 5):
		line1 += (" alone")		
	if line2.find(the, (len(line2) - 3), len(line2)) == (len(line2) - 3):
		line2 += random.choice(replacement)
	elif line2.find(india, (len(line2) - 2), len(line2)) == (len(line2) - 2):
		line2 += (" death")
	elif line1.find(so, (len(line2) - 5), len(line2)) == (len(line2) - 5):
		line2 += (" alone")			
	if line3.find(the, (len(line3) - 3), len(line3)) == (len(line3) - 3):
		line3 += random.choice(replacement)
	elif line3.find(india, (len(line3) - 2), len(line3)) == (len(line3) - 2):
		line3 += (" death")
	elif line3.find(so, (len(line3) - 5), len(line3)) == (len(line3) - 5):
		line3 += (" alone")			
	elif line3.find(of, (len(line3) - 2), len(line3)) == (len(line3) - 2):
		line3 += (" time")
	elif line3.find(either, (len(line3) - 2), len(line3)) == (len(line3) - 2):
		line3 += (" broken")
	elif line3.find(plus, (len(line3) - 3), len(line3)) == (len(line3) - 3):
		line3 += (" broken")
	
	blob1 = TextBlob(line1)
	blob2 = TextBlob(line2)
	blob3 = TextBlob(line3)
	unedited = line1 + " " + line2 + " " + line3
	poetry = blob1 + " " + blob2 + " " + blob3
	print poetry
	poetry = poetry.translate(to='es')
	poetry = poetry.translate(to='en')
	poetry = poetry.translate(to='nl')
	poetry = poetry.translate(to='en')
	print poetry
	blob1 = blob1.translate(to='es')
	blob1 = blob1.translate(to='en')
	blob1 = blob1.translate(to='nl')
	blob1 = blob1.translate(to='en')
	print blob1
	blob2 = blob2.translate(to='es')
	blob2 = blob2.translate(to='en')
	blob2 = blob2.translate(to='nl')
	blob2 = blob2.translate(to='en')
	print blob2
	blob3 = blob3.translate(to='es')
	blob3 = blob3.translate(to='en')
	blob3 = blob3.translate(to='nl')
	blob3 = blob3.translate(to='en')
	print blob3
	blob1 = str(blob1)
	blob2 = str(blob2)
	blob3 = str(blob3)
	
	poetry = str(poetry)
	novel.write(unedited)
	novel.write("\n")
	novel.write(poetry)
	novel.write("\n")
	novel.write(blob1)
	novel.write("\n")
	novel.write(blob2)
	novel.write("\n")
	novel.write(blob3)
	novel.write("\n")


file.close()	


