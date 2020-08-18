import spacy
import en_core_web_sm
from autocorrect import Speller
nlp = en_core_web_sm.load()
spell = Speller(lang='en')

# your sentences
x = "find me the nearest test center".lower()
old_y = "what is the nearest testing center to me".lower()

new_y = ''
z = 'find me the number of cases'

for word in old_y.split(' '):
    new_y += spell(word) + ' '
print(new_y)


search_doc = nlp(x)
main_doc = nlp(new_y)

main_doc2 = nlp(z)

print(main_doc.similarity(search_doc))
print(main_doc2.similarity(search_doc))