# -*- coding: utf-8 -*-
# title: word_freq_functions.py
# course: 언어와 컴퓨터
# author: 박수지
# date created: 2018-10-01
# description: 단어 빈도 계산하기


def get_word_list(sentence):
    '''문장을 받아서 단어 리스트를 반환하는 함수'''
    return sentence.strip().lower().split()

def remove_punct(word):
    '''단어를 받아서 문장부호를 제거하여 반환하는 함수'''
    return ''.join(char for char in word if char.isalnum())

def get_freq(seq):
    '''열을 받아서 {항목: 빈도} 딕셔너리를 반환하는 함수'''
    freq = {}
    for item in seq:
        if item in freq.keys():
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def get_word_freq(sentence):
    '''문장 문자열을 받아서 단어 빈도 딕셔너리를 반환하는 함수'''
    return get_freq(remove_punct(word) for word in get_word_list(sentence))

# 테스트
if __name__ == '__main__':
    sentences = ('Twinkle twinkle little star',
    'Baby shark, doo doo doo doo doo doo. Baby shark!')
    for sentence in sentences:
        print(sentence)
        print(get_word_freq(sentence))
