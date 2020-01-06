import os
import spacy

path = r'c:\users\jeff levy\documents\github\nlp_inflation\document.txt'
nlp = spacy.load('en_core_web_sm')

with open(path, 'r') as ifile:
    text = ifile.read()

doc = nlp(text)

inflation_tokens = [t for t in doc if 'inflation' in t.text]
inflation_ancestors = [list(t.ancestors) for t in inflation_tokens]
inflation_ancestors_text = [[t.text for t in ia] for ia in inflation_ancestors]

inflation_up = sum(['rise' in ia for ia in inflation_ancestors_text])
inflation_down = sum(['fall' in ia for ia in inflation_ancestors_text])

print('Mentions of inflation going up: {}\nMentions of inflation going down: {}'.format(inflation_up, inflation_down))
