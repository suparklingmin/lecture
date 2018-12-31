# -*- coding: utf-8 -*-
# title: decision_tree.py
# course: Language and Computer
# author: Suzi Park
# date created: 2018-10-29
# description: Decision tree

# list of abbreviations
abbre = ['Dr.', 'Mr.', 'Ms.']

# decision tree for eos determination
def iseos(word:str):
    if word.endswith(tuple('?!:')):
        return True
    if not word.endswith('.'):
        return False
    return word not in abbre

def eoslist(words:list):
    return [iseos(word) for word in words]

# non-recursive function
def sent_segment0(words:list):
    sents = []
    sent = ''
    for word, iseos in zip(words, eoslist(words)):
        sent += word
        if not iseos:
            sent += ' '
        else:
            sents.append(sent)
            sent = ''
    return sents

# recursive function
def sent_segment(words:list):
    # indices of eos
    eos_ind = [i for i, iseos in enumerate(eoslist(words)) if iseos]
    # stop condition
    if len(eos_ind) <= 1:
        return [' '.join(words)]
    # recursion
    for i in eos_ind:
        sent = ' '.join(words[:i+1])
        remainder = words[i+1:]
        return [sent] + sent_segment(remainder)

if __name__ == '__main__':
    text = "Hello! How are you, Mr. H? I'm fine, thank you. And you?"
    print(text)
    print("non-recursive :", sent_segment0(text.split()))
    print("recursive:", sent_segment(text.split()))
