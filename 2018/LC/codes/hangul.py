# -*- coding: utf-8 -*-
# title: hangul.py
# course: 언어와 컴퓨터
# author: 박수지
# date created: 2018-10-11
# description: 한글 처리 모듈 --- 음절 분해 및 자모 결합

# 1. 음절 분해
# 준비물
LEADING = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
VOWEL = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
TRAILING = ('',) + tuple('ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')

n_cnt = len(VOWEL) * len(TRAILING) # 588
t_cnt = len(TRAILING) # 28

syl = '햒'

# 음절의 지표
s_ind = ord(syl) - ord('가')

# 초성, 중성, 종성의 지표
l_ind = s_ind // n_cnt
v_ind = s_ind % n_cnt // t_cnt
t_ind = s_ind % n_cnt % t_cnt

jamos = ''
jamos += LEADING[l_ind]
jamos += VOWEL[v_ind]
jamos += TRAILING[t_ind]

jamos



# 2. 자모 결합
from unicodedata import name, lookup

# 알려진 사실
'''
>>> lookup('HANGUL CHOSEONG PANSIOS') + lookup('HANGUL JUNGSEONG ARAEA')
'ᅀᆞ'
'''

lvt = 'CHOSEONG', 'JUNGSEONG', 'JONGSEONG'


jamos = 'ㅈㅏㄹ'
l = lookup(name(jamos[0]).replace('LETTER', lvt[0]))
v = lookup(name(jamos[1]).replace('LETTER', lvt[1]))
t = lookup(name(jamos[2]).replace('LETTER', lvt[2]))
l + v + t


def jamo_name(jamo):
    return name(jamo).split()[-1]

jamos = 'ㅈㅏㄹ'
l = lookup(f'HANGUL {lvt[0]} {jamo_name(jamos[0])}')
v = lookup(f'HANGUL {lvt[1]} {jamo_name(jamos[1])}')
t = lookup(f'HANGUL {lvt[2]} {jamo_name(jamos[2])}')
l + v + t

#
jamo_names = 'CIEUC', 'A', 'RIEUL'
l = lookup(f'HANGUL {lvt[0]} {jamo_names[0]}')
v = lookup(f'HANGUL {lvt[1]} {jamo_names[1]}')
t = lookup(f'HANGUL {lvt[2]} {jamo_names[2]}')
l + v + t

#
jamo_names = 'PANSIOS', 'ARAEA', 'RIEUL'
l = lookup(f'HANGUL {lvt[0]} {jamo_names[0]}')
v = lookup(f'HANGUL {lvt[1]} {jamo_names[1]}')
t = lookup(f'HANGUL {lvt[2]} {jamo_names[2]}')
l + v + t

# 'ㅈ' -> 'CIEUC'
# 'ㅏ' -> 'A'
# 'ㄹ' -> 'RIEUL'
# ??? -> 'PANSIOS'
# ??? -> 'ARAEA'
def jamo_name(jamo):
    yet_dict = {'Z': 'PANSIOS', 'A': 'ARAEA', 'V': 'KAPYEOUNPIEUP', 'K': 'PIEUP-SIOS-KIYEOK', 'T': 'PIEUP-SIOS-TIKEUT'}
    if jamo in yet_dict.keys():
        return yet_dict[jamo]
    else:
        return name(jamo).split()[-1]

'''
>>> jamo_name("ㅈ")
'CIEUC'
>>> jamo_name("ㅏ")
'A'
>>> jamo_name("ㄹ")
'RIEUL'
>>> jamo_name("Z")
'PANSIOS'
>>> jamo_name("A")
'ARAEA'
'''

jamos = 'ZAㄹ'
l = lookup(f'HANGUL {lvt[0]} {jamo_name(jamos[0])}')
v = lookup(f'HANGUL {lvt[1]} {jamo_name(jamos[1])}')
t = lookup(f'HANGUL {lvt[2]} {jamo_name(jamos[2])}')
l + v + t
# 'ᅀᆞᆯ'

# 반복을 없애자
syl = ''
for p, j in zip(lvt, jamos):
    syl += lookup(f'HANGUL {p} {jamo_name(j)}')

# 더 간단하게
''.join(lookup(f'HANGUL {p} {jamo_name(j)}') for p, j in zip(lvt, jamos))

# 함수로
def conjoin(jamos):
    return ''.join(lookup(f'HANGUL {p} {jamo_name(j)}') for p, j in zip(lvt, jamos))

 
'''
>>> conjoin('ㅈㅏㄹ')
'잘'
>>> conjoin('ZAㄹ')
'ᅀᆞᆯ'
>>> conjoin('Kㅜㄹ')
'ᄢᅮᆯ'
>>> conjoin('TAㄹ')
'ᄣᆞᆯ'
'''
