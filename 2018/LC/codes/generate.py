# -*- coding: utf-8 -*-
# title: generate.py
# course: Language and Computer
# author(s): Suzi Park
# date created: 2018-11-13
# description: word autocomplete and generation

from pprint import pprint
from collections import defaultdict, Counter
from random import choice

text = '''i like to eat pasta .
i want to eat food from malaysia .
show me the list again .
i 'd like the previous list please .
i 'd like to go to a japanese restaurant .'''

# sents: list of sentences(list of words)
sents = [n.split() for n in text.split('\n')] # you should edit this line
pprint(sents)

bigrams_dict = defaultdict(list)
for sent in sents:
    filled_sent = ['<s>'] + sent
    for wd1, wd2 in zip(filled_sent, filled_sent[1:]):
        bigrams_dict[wd1].append(wd2)

pprint(bigrams_dict)
pprint(Counter(choice(bigrams_dict['<s>']) for _ in range(100)))

def modes(seq):
    counts = Counter(seq)
    M = max(counts.values())
    return [item for item, count in counts.items() if count == M]

def complete():
    # first word
    wd = choice(modes(bigrams_dict['<s>']))
    # initialize sentence to be completed
    completed = [wd]
    while wd != '.':
        wd = choice(modes(bigrams_dict[wd]))
        completed.append(wd)
    return ' '.join(wd for wd in completed)

for _ in range(10):
    print(complete())

def generate():
    # first word
    wd = choice(bigrams_dict['<s>'])
    # initialize sentence to be completed
    generated = [wd]
    while wd != '.':
        wd = choice(bigrams_dict[wd])
        generated.append(wd)
    return ' '.join(wd for wd in generated)

for _ in range(10):
    print(generate())
