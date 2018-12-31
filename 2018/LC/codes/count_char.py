# -*- coding: utf-8 -*-
# 문장 내에서 특정 글자의 개수를 세는 프로그램
sentence = input('문장을 입력하세요: ')
char = input('찾고 싶은 글자를 입력하세요: ')
n = sentence.lower().count(char.lower())
print('{}의 출현 횟수: {}'.format(char, n))
