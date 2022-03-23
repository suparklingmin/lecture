# 컴퓨터언어학

2022학년도 1학기 서울대학교 언어학과 전공필수

## 교수자

박수지 (mam3b at snu.ac.kr, https://github.com/suzisuti)

## 목표

[컴퓨터언어학] (108.413A)에서는 심층학습(딥러닝, 인공신경망)을 사용한 자연어처리 기법을 소개한다. 이 과목을 이수함으로써 수강생들은 여러 가지 인공신경망 모형들의 개략적인 원리를 이해하고 자연어처리 분야의 구체적인 과제를 해결하는 데 이를 활용할 수 있게 될 것이다. 이 강좌의 전반부에서는 로지스틱 회귀분석에 대한 이해를 바탕으로 순방향신경망(FFNN)과 합성곱신경망(CNN)에 대해 배우며, 이를 통해 주어진 영화평이 긍정적인지 부정적인지를 자동으로 분류하는 모형을 pytorch로 구현한다. 후반부에서는 순환신경망(RNN)을 응용하여 단어 사이의 문맥 정보를 포착하는 기법을 알아보고, 현재 다양한 자연어처리 과제에서 좋은 성능을 보이는 BERT와 GPT-2,3 등의 사전학습 언어모형(PLM)을 활용하는 방법을 익힌다.

## 교재

+ 주교재: Dan Jurafsky and James H. Martin. (Dec 29, 2021). *Speech and Language Processing.* (3rd ed. draft) https://web.stanford.edu/~jurafsky/slp3/
+ 부교재: 사이토 고키. (2017). 밑바닥부터 시작하는 딥러닝. 한빛미디어. https://github.com/WegraLee/deep-learning-from-scratch
+ 부교재: 사이토 고키. (2019). 밑바닥부터 시작하는 딥러닝 2. 한빛미디어. https://github.com/WegraLee/deep-learning-from-scratch-2


## 수업 일정 및 자료

### 제1강 (2022-03-02) 강좌 소개

---

### 제2강 (2021-03-07) NumPy 실습: 행렬과 벡터

---

### 제3강 (2021-03-14) 로지스틱 회귀분석 (1)

[SLP3 Ch. 5 Logistic Regression](https://web.stanford.edu/~jurafsky/slp3/5.pdf)

#### 슬라이드

---

### 제4강 (2021-03-16) 로지스틱 회귀분석 (2)

#### 슬라이드

---

### 5강 (2022-03-21) SLP3 6.1-5 벡터 의미론: 어휘 의미론과 단어 벡터, 코사인 유사도, TF-IDF, PMI6

---

### 6강 (2022-03-23) SLP3 6.6-8 벡터 의미론: Word2Vec, 단어 임베딩의 해석 및 활용

---

### 7강 (2022-03-28) SLP3 7.1-2 신경망 언어 모형: 계산 유닛, XOR 문제

---

### 8강 (2022-03-30) SLP3 7.3-4 신경망 언어 모형: 순방향 신경망(FFNN)의 구성 요소

---

### 9강 (2022-04-04) SLP3 7.5-6 신경망 언어 모형: FFNN 모형의 구성 및 훈련 방법

---

### 10강 (2022-04-06) SLP3 7.6-7 신경망 언어 모형: FFNN 언어 모형

---

### 11강 (2022-04-11) 밑바닥부터 시작하는 딥러닝 (1) 7장: CNN

---

### 12강 (2022-04-13) Kim (2014) “Convolutional Neural Networks for Sentence Classification”

---

### 13강 (2022-04-20) [실습] PyTorch: 텐서 연산 및 FFNN 구현

---

### 14강 (2022-04-26) SLP3 9.1-5 단순 순환 신경망(Simple RNN)

---

### 15강 (2022-04-28) SLP3 9.6 장단기기억 순환 신경망 (LSTM)

---

### 16강 (2022-05-02) SLP3 9.7–9 Self-Attention Networks: 트랜스포머

---

### 17강 (2022-05-04) [실습] PyTorch: RNN 구현

---

### 18강 (2022-05-09) SLP3 10.1,7-9 기계번역

---

### 19강 (2022-05-11) SLP3 10.2-3 Encoder-decoder (seq2seq)

---

### 20강 (2022-05-16) SLP3 10.4, 6 Encoder-decoder with Attentions

---

### 21강 (2022-05-18) [실습] PyTorch: seq2seq 구현

---

### 22강 (2022-05-23) SLP3 11.1-2 Bidirectional Encoders and Pre-Training

---

### 23강 (2022-05-25) SLP3 11.3 Transfer Learning through Fine-Tuning

---

### 24강 (2022-05-30) [실습] HuggingFace: 데모 (Pipeline)

---

### 25강 (2022-06-08) [실습] HuggingFace: 훈련 (Datasets, TrainingArguments)

---
