# -*- coding: utf-8 -*-
password = input('패스워드를 입력하세요: ')
if len(password) < 8:
    print('너무 짧습니다.')
elif password.isalpha():
    print('숫자나 특수문자를 포함하세요.')
else:
    print('좋습니다.')
