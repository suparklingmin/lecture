# -*- coding: utf-8 -*-
# title: ngrams.py
# course: Language and Computer
# author(s): Suzi Park
# date created: 2018-11-04
# description: "English-y" word generation based on character N-grams

from random import choice
from collections import Counter

with open('literary.txt') as f:
    words = ['^'+line.strip().lower()+'$' for line in f if not line.startswith('#')]

# Bigrams

bigrams = [(ch1, ch2) for word in words for ch1, ch2 in zip(word, word[1:])]
bigram_keys = {ch1 for ch1, ch2 in bigrams}
bigram_dict = {key: [ch2 for ch1, ch2 in bigrams if ch1 == key] for key in bigram_keys}

def generate_from_bigrams(start='^'):
    word = start
    char = choice(bigram_dict[start])
    while char != '$':
        word += char
        char = choice(bigram_dict[char])
    if len(word) > 4:
        return word.replace('^', '')
    else:
        return generate_from_bigrams(start)

print("From bigrams:")
print([generate_from_bigrams() for _ in range(30)])


# Trigrams

words = ['^' + word for word in words]
trigrams = [(ch1 + ch2, ch3) for word in words for ch1, ch2, ch3 in zip(word, word[1:], word[2:])]
trigram_keys = {ch12 for ch12, ch3 in trigrams}
trigram_dict = {key: [ch3 for ch12, ch3 in trigrams if ch12 == key] for key in trigram_keys}

def generate_from_trigrams(start='^^'):
    word = start
    char = choice(trigram_dict[start])
    while char != '$':
        word += char
        char = choice(trigram_dict[word[-2:]])
    return word.replace('^', '') if len(word) > 4 else generate_from_trigrams(start)

print("From trigrams:")
print([generate_from_trigrams() for _ in range(30)])


# Quadrigrams (4-grams)

words = ['^' + word for word in words]
quadrigrams = [(ch1 + ch2 + ch3, ch4) for word in words for ch1, ch2, ch3, ch4 in zip(word, word[1:], word[2:], word[3:])]
quadrigram_keys = {ch123 for ch123, ch4 in quadrigrams}
quadrigram_dict = {key: [ch4 for ch123, ch4 in quadrigrams if ch123 == key] for key in quadrigram_keys}

def generate_from_quadrigrams(start='^^^'):
    word = start
    char = choice(quadrigram_dict[word[-3:]])
    while char != '$':
        word += char
        char = choice(quadrigram_dict[word[-3:]])
    if len(word) > 5 and word +'$' not in words:
        return word.replace('^', '')
    else:
        return generate_from_quadrigrams(start)

print("From 4-grams:")
print([generate_from_quadrigrams() for _ in range(30)])

