# -*- coding: utf-8 -*-
# title: reg_exp.py
# course: Language and Computer
# author(s): Suzi Park
# date created: 2018-10-29
# description: Learning re module

import re

# 1. 정규표현식 패턴 만들기
# XX대학 XX학(부)
# 주의: 작곡과 등 "학"이 없는 학과명 존재
pattern = re.compile(r'([가-힣]+대학 )?[가-힣]+학?[과부]')


# 2. 패턴과 매치되는 것 찾기
string = '서울대학교 자연과학대학 수리과학부 이한솔'

print(pattern.search(string))
print(re.search(pattern, string)) # 위와 같음

print(pattern.match(string)) # 문자열 첫 부분부터 매치되어야 함

match = pattern.search(string)
print(match.group()) # 매치되는 부분 전체
print(match.group(1)) # 괄호 속에 있던 것

pattern = re.compile(r'(?:[가-힣]+대학 )?[가-힣]+학?[과부]')
match = pattern.search(string)
print(match.group()) # 매치되는 부분 전체
print(match.group(1)) # IndexError

pattern = re.compile(r'(?:([가-힣]+)대학 )?([가-힣]+)학?[과부]')
match = pattern.search(string)
print(match.group()) # 매치되는 부분 전체
print(match.group(1))
print(match.group(2))


# 3. 패턴과 매치되는 것들의 리스트 반환하기
# 신문 이름을 모두 찾기
pattern = re.compile(r'([가-힣]+(?:일보|신문))')

# http://news.khan.co.kr/kh_news/khan_art_view.html?art_id=200510041802191
string = """조선일보는 지난달 28일자 A2면에 기사표절 사과문을 실었다. \
조선일보는 ‘기사 표절 사과합니다’란 제목의 사과문에서 “지난 14일자 본지 \
A14면에 게재된 ‘강남아파트 여전히 재산세 적다’ 제하의 기사 내용 중 대부분이 \
지난 12일자 경향신문 2면에 게재된 ‘강남 재산세 턱없이 덜 낸다’ 제하의 기사를 \
표절해 작성한 것이었음이 본사 내부조사 결과 확인됐다”고 밝혔다. 사과문은 “독자 \
여러분께 심심한 사과를 드리며 용서를 구한다”며 “경향신문사와 담당기자에게도 정중히 \
사과한다”고 말했다. 이어 “앞으로 이런 일이 재발하지 않도록 내부적으로 문책하는 한편 \
취재와 기사 작성에 더욱 세심한 주의와 정성을 쏟겠다”고 덧붙였다. 

조선일보의 경향신문 기사 표절 의혹은 지난달 24일 미디어비평 프로그램인 KBS 1TV의 \
‘미디어 포커스’를 통해 제기된 뒤 ‘기자협회보’ 등에서도 잇달아 보도했다. 

이에 앞서 문화일보도 지난달 26일자 1면에 “‘기사 표절’ 정중히 사과드립니다”라는 사과문을 실었다.

문화일보는 “9월23일자 5면에 게재된 ‘반미(反美) 만화 평통 공모전 대상 수상 논란’ 기사가 \
같은날 조선일보 A4면에 게재된 ‘평통 청소년 통일만화 공모전－反美 만화가 대상 받았다’ 기사와 \
사실상 똑같은 일이 발생했다”고 밝혔다. 사과문은 “누를 끼친 조선일보사와 담당기자에게도 정중히 \
사과드린다”며 “전화위복의 계기로 삼도록 하겠다”고 덧붙였다."""

print(pattern.search(string).group()) # 첫 번째 매치
print(pattern.findall(string)) # 매치된 문자열 전체의 리스트


# 4. 패턴과 매치되는 것 바꾸기
# 2018년 10월 31일 11시 -> #년 #월 #일 #시
string = '2018년 10월 31일 11시'
print(string)
print(re.sub(r'[0-9]+', '#', string)) # 사실 패턴 자리에 문자열을 쓸 수 있음

# 02-880-2206 -> (02)880-2206
string = '02-880-2206'
print(string)
print(re.sub(r'(0[02-9][0-9]*)-([0-9]+-[0-9]+)', r'(\1)\2', string))

