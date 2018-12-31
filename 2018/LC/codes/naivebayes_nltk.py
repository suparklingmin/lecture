# -*- coding: utf-8 -*-
# title: naivebayes_nltk.py
# course: Language and Computer
# author(s): Suzi Park
# date created: 2018-11-21
# description: implementing naive bayes classifier using sciket-learn

# http://www.nltk.org/book/ch06.html

# 먼저 할 일: nltk 설치하기

from random import seed, shuffle
import nltk

# 0. 코퍼스 준비
# 0.1. 파일 읽기
f = open('reviews.txt', 'r', encoding='utf-8')
# 정답과 데이터 분리하기
data = [line.split('\t') for line in f]
data = [(int(cat), doc.split()) for cat, doc in data]
f.close()

# 0.2. 순서 섞기
seed(208)
shuffle(data)

# 0.3. 코퍼스 분할하기
# 코퍼스의 10%를 실험 집합으로, 다음 10%를 개발 집합으로, 나머지를 훈련 집합으로 삼기
boundary = int(len(data) * 0.1)
test = data[:boundary]
dev = data[boundary:2*boundary]
train = data[2*boundary:]

# 1. 단순 베이즈 분류기 학습
# 1.1. 훈련 집합의 어휘 목록
vocabulary = {morph for cat, doc in train for morph in doc}

# 문서(doc)을 받아 단어를 키로, 단어가 문서에 있는지를 값으로 하는 딕셔너리를 반환하는 함수
def get_features(doc):
	return {word: word in doc for word in vocabulary}

# 1.2. [({속성: 값}, 정답)] 꼴로 만들기
train_set = [(get_features(doc), cat) for cat, doc in train]
test_set = [(get_features(doc), cat) for cat, doc in test]
dev_set = [(get_features(doc), cat) for cat, doc in dev]


clf_nb = nltk.NaiveBayesClassifier.train(train_set)
clf_nb.show_most_informative_features()

# 2. 개발
nltk.classify.accuracy(clf_nb, dev_set)

# 오류 분석
for cat, doc in dev:
	predicted = clf_nb.classify(get_features(doc))
	if cat != predicted:
		print(cat, doc)


# 3. 최대 엔트로피 분류기 학습
clf_me = nltk.MaxentClassifier.train(train_set, max_iter=50)
clf_me.show_most_informative_features()

# 4. 개발
nltk.classify.accuracy(clf_me, dev_set)

# 오류 분석
for cat, doc in dev:
	predicted = clf_me.classify(get_features(doc))
	if cat != predicted:
		print(cat, doc)



# 3'. 새로운 시도: 실질어 및 이모티콘만 반영하기
def get_features2(doc):
	return {word: word in doc for word in vocabulary if word.endswith(('NNG', 'VA', 'VV', 'XR', 'MAG', 'EMO'))}

# 속성 집합 업데이트
train_set = [(get_features2(doc), cat) for cat, doc in train]
test_set = [(get_features2(doc), cat) for cat, doc in test]
dev_set = [(get_features2(doc), cat) for cat, doc in dev]

# 재학습
clf_me = nltk.MaxentClassifier.train(train_set, max_iter=50)
clf_me.show_most_informative_features()

# 개발
nltk.classify.accuracy(clf_me, dev_set)

# 오류 분석
for cat, doc in dev:
	predicted = clf_me.classify(get_features2(doc))
	if cat != predicted:
		print(cat, doc)



# 3''. 새로운 시도: 후반부의 내용을 반영하기
def get_features3(doc):
	return {word: word in doc[:len(doc)//2] for word in vocabulary}

# 속성 집합 업데이트
train_set = [(get_features3(doc), cat) for cat, doc in train]
test_set = [(get_features3(doc), cat) for cat, doc in test]
dev_set = [(get_features3(doc), cat) for cat, doc in dev]

# 재학습
clf_me = nltk.MaxentClassifier.train(train_set, max_iter=50)
clf_me.show_most_informative_features()

# 개발
nltk.classify.accuracy(clf_me, dev_set)

# 오류 분석
for cat, doc in dev:
	predicted = clf_me.classify(get_features3(doc))
	if cat != predicted:
		print(cat, doc)



# 3'''. 새로운 시도: 단어 빈도를 세기
def get_features4(doc):
	return {word: doc.count(word) for word in vocabulary}

# 속성 집합 업데이트
train_set = [(get_features4(doc), cat) for cat, doc in train]
test_set = [(get_features4(doc), cat) for cat, doc in test]
dev_set = [(get_features4(doc), cat) for cat, doc in dev]

# 재학습
clf_me = nltk.MaxentClassifier.train(train_set, max_iter=50)
clf_me.show_most_informative_features()

# 개발
nltk.classify.accuracy(clf_me, dev_set)

# 오류 분석
for cat, doc in dev:
	predicted = clf_me.classify(get_features4(doc))
	if cat != predicted:
		print(cat, doc)

