# -*- coding: utf-8 -*-
# title: maxmatch.py
# course: 언어와 컴퓨터
# author: 박수지
# date created: 2018-10-25
# description: MaxMatch 알고리듬

# 단어 목록
words = ['가방', '방', '아버지', '가', '에', '들어가신다']

def maxmatch(sentence:str, dictionary:list):
    # stop condition
    if not sentence:
        return []
    # recursion
    for i in range(len(sentence), 0, -1):
        first_word, remainder = sentence[:i], sentence[i:]
        if first_word in dictionary:
            return [first_word] + maxmatch(remainder, dictionary)
    # out-of-vocabulary
    first_word = sentence[:1]
    remainder = sentence[1:]
    return [first_word] + maxmatch(remainder, dictionary)

if __name__ == '__main__':
    print(maxmatch('아버지가방에들어가신다', words))
    print(maxmatch('방에아버지가들어가신다', words))
    print(maxmatch('아버지가가방에들어가신다', words))
    print(maxmatch('할아버지가큰방에들어가신다', words))
