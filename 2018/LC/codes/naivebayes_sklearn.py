# -*- coding: utf-8 -*-
# title: naivebayes_sklearn.py
# course: Language and Computer
# author(s): Suzi Park
# date created: 2018-11-21
# description: implementing naive bayes classifier using sciket-learn

# https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

# 먼저 할 일: sklearn 설치하기

from random import seed, shuffle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn import metrics


# 0. 코퍼스 준비
# 0.1. 파일 읽기
f = open('reviews.txt', 'r', encoding='utf-8')
# 정답과 데이터 분리하기
data = [line.split('\t') for line in f]
f.close()
# sklearn을 사용할 때는 문서를 단어의 리스트로 만들 필요가 없다.

# 0.2. 순서 섞기
seed(208)
shuffle(data)

# 0.3. 훈련 집합과 실험 집합으로 분할하기
# 코퍼스의 10%를 실험 집합으로, 다음 10%를 개발 집합으로, 나머지를 훈련 집합으로 삼기
boundary = int(len(data) * 0.1)
test = data[:boundary]
dev = data[boundary:2*boundary]
train = data[2*boundary:]


# 1. 훈련
# 훈련 집합을 설명 변수 벡터의 행렬 X와 반응 변수 벡터 y로 표현하기
y = [int(item[0]) for item in train]
# 훈련 집합의 문서 목록
docs_train = [item[1] for item in train]
# 각 문서를 형태소 출현 횟수의 벡터로 표현하기
vectorizer = CountVectorizer(input='content', lowercase=False, token_pattern='(?u)\\S+')
X = vectorizer.fit_transform(docs_train) 
'''
>>> vectorizer.get_feature_names()[100:110]
['개봉/NNG', '개연성/NNG', '개판/NNG', '갤가돗/UN', '갱/NNG', '걍/MAG', '거/NNB', '거든요/EFN', '거지/NNG', '건/NNM']
>>> X.shape # 87개 문서, 998개 어휘
(87, 998)
>>> X.toarray()
array([[0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       ...,
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0]], dtype=int64)
>>> X.max()
11
'''

# 단순 베이즈 분류기 훈련하기
clf = MultinomialNB()
# clf = LogisticRegression() # 로지스틱 회귀분석으로 훈련하기
clf.fit(X, y)


# 2. 개발
# 정답 벡터
gold_dev = [int(item[0]) for item in dev]
docs_dev = [item[1] for item in dev]
mat_dev = vectorizer.transform(docs_dev)
predicted_dev = clf.predict(mat_dev)

# 3. 평가
print(np.transpose(np.concatenate([[gold_dev], [predicted_dev]])))
print(metrics.confusion_matrix(gold_dev, predicted_dev))
print(f'Accuracy: {np.mean(gold_dev == predicted_dev)}')
print(metrics.classification_report(gold_dev, predicted_dev))



# 2'. 재개발: 평탄화 없이 학습해 보면 어떨까?
clf = MultinomialNB(alpha=0)
clf.fit(X, y)

# 3'. 재평가
predicted_dev = clf.predict(mat_dev)
print(np.transpose(np.concatenate([[gold_dev], [predicted_dev]])))
print(metrics.confusion_matrix(gold_dev, predicted_dev))
print(f'Accuracy: {np.mean(gold_dev == predicted_dev)}')
'''Accuracy: 0.6666666666666666 --- 평탄화를 하는 것이 좋다.'''
print(metrics.classification_report(gold_dev, predicted_dev))


# 2''. 다른 발상: 바이그램을 추가해 보자.
vectorizer2 = CountVectorizer(input='content', lowercase=False, token_pattern='(?u)\\S+', ngram_range=(1,2))
X = vectorizer2.fit_transform(docs_train) 
'''
>>> vectorizer.get_feature_names()[100:110]
['갤가돗/UN', '걍/MAG', '거/NNB', '거든요/EFN', '건/NNM', '건만/ECE', '걸/VV', '겁/NNG', '것/NNB', '게/ECD']
>>> X.shape
(79, 3256)
>>> X.toarray()
array([[0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       ...,
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0]], dtype=int64)
>>> X.max()
11
'''

# 단순 베이즈 분류기 훈련하기
clf = MultinomialNB()
clf.fit(X, y)

# 실험 집합의 문서를 훈련 집합의 문서와 같은 차원의 벡터로 변환하기
mat_dev = vectorizer2.transform(docs_dev)
'''
>>> mat_dev.shape 
(9, 3256)
'''

# 훈련한 모형으로 실험 집합 문서들의 범주를 예측하기
predicted_dev = clf.predict(mat_dev)

# 3''. 재재평가
# 정답과 예측 대조
print(np.transpose(np.concatenate([[gold_dev], [predicted_dev]])))
print(metrics.confusion_matrix(gold_dev, predicted_dev))
print(f'Accuracy: {np.mean(gold_dev == predicted_dev)}') # 1.0!
print(metrics.classification_report(gold_dev, predicted_dev))

# Accuracy가 1이 나왔다! --- 이 모형을 선택하자.



# 그런데 실험 집합에서도 잘 작동하는가?
# 4. 실험
gold_test = [int(item[0]) for item in test]
docs_test = [item[1] for item in test]
mat_test = vectorizer2.transform(docs_test)
'''
>>> mat_test.shape
(9, 3256)
'''

# 훈련한 모형으로 실험 집합 문서들의 범주를 예측하기
predicted_test = clf.predict(mat_test)

# 5. 평가
print(np.transpose(np.concatenate([[gold_test], [predicted_test]])))
print(metrics.confusion_matrix(gold_test, predicted_test))
print(f'Accuracy: {np.mean(gold_test == predicted_test)}') # 0.6666666
print(metrics.classification_report(gold_test, predicted_test))
# 정확도가 0.6으로 오히려 떨어졌지만 실험 집합의 결과를 보고 훈련 방식을 바꾸는 것은 부정행위
