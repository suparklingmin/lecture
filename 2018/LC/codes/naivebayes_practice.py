# -*- coding: utf-8 -*-
# title: naivebayes_practice.py
# course: Language and Computer
# author(s): Suzi Park
# date created: 2018-11-20
# description: naive bayes classifier

# from konlpy.tag import Kkma # 형태소 분석
from random import seed, shuffle
from collections import Counter, defaultdict
from scipy import log, argmax


# -1. 형태소 분석
# f = open('reviews_raw.txt', 'r', encoding='utf-8')
# data = [line.split('\t') for line in f]
# kkma = Kkma() # 형태소 분석기
# data = [(c, ['/'.join(pair) for pair in kkma.pos(d.strip())]) for c, d in data]
# g = open('reviews.txt', 'w', encoding='utf-8')
# g.writelines('\t'.join((c, ' '.join(morph for morph in d))) + '\n' for c, d in data)
# g.close()
# f.close()

# 0. 코퍼스 준비
# 0.1. 파일 읽기
f = open('reviews.txt', 'r', encoding='utf-8')
# 정답과 데이터 분리하기
data = [line.split('\t') for line in f] 
# 문서를 형태소의 리스트로 바꾸기
# c for class(sentiment), doc for document(review)
data = [(int(c), doc.split()) for c, doc in data]
f.close()

# 0.2. 순서 섞기
seed(208)
shuffle(data)

'''
>>> data[0]
(0, ['졸/VV', '려요/ECD', '../SW', '배트/NNG', '맨/NNG', '과/JKM', '슈퍼맨/NNG', '의/JKG', '갑작스럽/VA', 'ㄴ/ETD', '화해/NNG', '??/SW', '뭐/NP', '여/NNG', '??/SW', '루이스/NNG', '는/JX', '또/MAG', '뭐/NP', '여/NNG', '??/SW', '민폐/NNG', '캐릭/NNG', '??/SW', '애/NNG', '니/JC', '다크/UN', '나이트/NNG', '리턴즈/UN', '와/JKM', '두/VV', 'ㅁ/ETN', '스/VV', '데/EFN', '이의/NNG', '짬뽕/NNG', '생뚱맞/VA', '게/ECD', '나타나/VV', '는/ETD', '원/NNM', '드/VV', '어/ECS', '우먼/NNG', '총/MDT', '1/NR', '분/NNM', '미만/NNG', '의/JKG', '출연/NNG', '아쿠아/NNG', '맨/NNG', '과/JKM', '한명/NNG', '더/MAG', '../SW', '기대/NNG', '하/XSV', '지/ECD', '마시/VV', '고/ECE', '보시/VV', '어야/ECD', '하/VV', 'ㅂ니다/EFN'])
'''

# 0.3. 훈련 집합과 실험 집합으로 분할하기
boundary = int(len(data) * 0.9)
# 코퍼스의 90%를 훈련 집합으로, 나머지 10%를 실험 집합으로 삼기
train = data[:boundary]
test = data[boundary:]


# 1. 훈련 집합에서 로그사전확률 P(c) 구하기
# 1.1. 문서 개수
Nc = Counter() # edit this line
Ndoc = len(train)
'''
>>> Nc
Counter({1: 47, 0: 40})
>>> Ndoc
87
'''

# 1.2. 로그사전확률
logprior = {} # edit this line
'''
>>> logprior
{0: -0.7770286645406475, 1: -0.6157605169445252}
'''


# 2. 훈련 집합에서 로그가능도 P(w|c) 구하기
# 2.1. 훈련 집합의 어휘 목록
vocabulary = []
# edit this line
# edit this line
# edit this line
# edit this line

'''
>>> len(vocabulary)
998
>>> vocabulary[:5]
['졸/VV', '려요/ECD', '../SW', '배트/NNG', '맨/NNG']
'''

# 2.2. 범주별로 문서 합치기
bigdoc = defaultdict(list)
# edit this line
# edit this line

'''
>>> bigdoc[1][-5:]
['좋/VA', 'ㄹ/ETD', '멋/NNG', '짐/NNG', '!!!/SW']
>>> bigdoc[0][-5:]
['졸리/VV', '어/ECS', '디지/VV', '는/ETD', '줄/NNG']
'''

# 2.3. 범주별 "큰 문서"에서 어휘 출현 횟수 세기
counts = defaultdict(Counter)
# edit thisline
# edit thisline

# 2.4. Add-1 smoothing
for w in vocabulary:
	for c in counts:
		counts[c][w] += 1

'''
>>> counts[1].most_common(5)
[('이/VCP', 32), ('ㄴ/ETD', 30), ('./SF', 27), ('하/XSV', 27), ('의/JKG', 25)]
>>> counts[0].most_common(5)
[('./SF', 52), ('ㄴ/ETD', 43), ('하/XSV', 40), ('고/ECE', 28), ('의/JKG', 24)]
'''

# 2.5. 로그가능도
loglikelihood = defaultdict(dict)
for c, counter in counts.items():
	count_c = 1 # edit this line
	for w in vocabulary:
		loglikelihood[w][c] = 0 # edit this line

'''
>>> loglikelihood['재밌/VA']
{0: -7.861341795599989, 1: -5.990630866359405}
>>> loglikelihood['재미/NNG']
{0: -6.762729506931879, 1: -6.396095974467569}
>>> loglikelihood['잼/NNG']
{0: -7.861341795599989, 1: -5.702948793907623}
>>> loglikelihood['분위기/NNG']
{0: -7.1681946150400435, 1: -5.702948793907623}
>>> loglikelihood['울/VV']
{0: -6.251903883165888, 1: -7.7823903355874595}
>>> loglikelihood['차라리/MAG']
{0: -6.475047434480098, 1: -7.7823903355874595}
>>> loglikelihood['알바/NNG']
{0: -6.475047434480098, 1: -7.7823903355874595}
>>> loglikelihood['지루/XR']
{0: -6.0695823263719335, 1: -7.089243155027514}
'''

# 3. 실험 집합에서 범주 예측하기
results = []
for real, testdoc in test:
	sums = {} # edit this line
	# edit this line
	# edit this line
	# edit this line
	# edit this line
	predict = 0 # edit this line
	results.append({real, predict})

'''
>>> results
[(0, 0), (0, 1), (0, 0), (1, 1), (0, 0), (0, 0), (1, 1), (1, 1), (0, 1), (1, 0)]
'''

accuracy = sum(1 for real, predict in results if real == predict) / len(results)
precision_pos = sum(1 for real, predict in results) / sum(1 for real, predict in results) # edit this line
precision_neg = sum(1 for real, predict in results) / sum(1 for real, predict in results) # edit this line
recall_pos = sum(1 for real, predict in results) / sum(1 for real, predict in results) # edit this line
recall_neg = sum(1 for real, predict in results) / sum(1 for real, predict in results) # edit this line

'''
>>> accuracy, precision_pos, precision_neg, recall_pos, recall_neg
(0.7, 0.6, 0.8, 0.75, 0.6666666666666666)
'''