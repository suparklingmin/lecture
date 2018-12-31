# -*- coding: utf-8 -*-
n = input('정수를 입력하세요: ')
if n.isnumeric() and (int(n) % 3):
    print('3의 배수가 아닙니다.')
if n.isnumeric() and not (int(n) % 3):
    print('3의 배수입니다.')
if not n.isnumeric():
    print('정수를 입력하지 않았습니다.')
