from string import digits
file = open('forestry2.txt', 'r')

lowercase = file.read()
lowercase = str(lowercase)
#lowercase = lowercase.lower()
file.close()

result = lowercase.translate(None, digits)

#result = result.translate(None, punctuation)

file = open('forestry2.txt', 'w')
file.seek(0)
file.truncate()
file.write(result)
file.close()
