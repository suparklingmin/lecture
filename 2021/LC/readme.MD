# 언어와 컴퓨터 

2021학년도 2학기 서울대학교 언어학과 전공탐색

## 교수자

박수지 (mam3b at snu.ac.kr, https://github.com/suzisuti)

## 목표

[언어와 컴퓨터] (100.130)는 [컴퓨터언어학] (108.413A)의 선수과목으로, 심층학습(딥러닝, 인공신경망)을 사용한 자연언어처리 기법을 학습하기 위해 필요한 컴퓨터언어학의 기본 지식을 습득하는 것을 목표로 한다. 이 과목을 이수함으로써 학생들은 인공신경망 모형이 도입되기 전까지 자연언어처리 분야에서 전통적으로 어떤 기법을 사용하고 어떤 과제를 처리했는지를 이해하고 파이썬으로 구현할 수 있게 될 것이다. 이 강좌의 전반부에서는 파이썬의 기초와 정규표현식에 대해 배우며, 이를 통해 최초의 규칙 기반 챗봇인 ELIZA를 구현한다. 후반부에서는 기계학습과 벡터 의미론에서 대해 배우며, 이를 활용하여 주어진 트위터 데이터가 악성 트윗인지 아닌지를 자동으로 예측하는 모형을 개발한다.

이 강좌에서는 수강생을 대학 입학 후 수학을 따로 공부하지 않은 인문대학 1–2학년생으로 가정하고, 후반부 수업은 조건부확률, 로그함수, 지수함수 등 기초적인 내용을 복습하는 데서 시작할 것이다.

## 교재

+ Dan Jurafsky and James H. Martin. (September 21, 2021). *Speech and Language Processing.* (3rd ed. draft) https://web.stanford.edu/~jurafsky/slp3/

## 수업 일정 및 자료

### 제1강 (2021-09-01) 강의 소개 및 파이썬 시작

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/01-20210901.pdf)

#### 참고 자료

+ [Eliza, Computer Therapist](http://psych.fullerton.edu/mbirnbaum/psych101/Eliza.htm)
+ [Sentiment Analysis - AllenNLP - Demo](https://demo.allennlp.org/sentiment-analysis/glove-sentiment-analysis)
+ [Korean Word2Vec](https://word2vec.kr/)

---

### 제2강 (2021-09-06) 파이썬 기본 문법

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/02-20210906.pdf)

---

### 제3강 (2021-09-08) 반복 가능한 자료형

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/03-20210908.pdf)

---

### 제4강 (2021-09-13) 반복문

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/04-20210913.pdf)

---

### 제5강 (2021-09-15) 조건문

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/05-20210915.pdf)

---

### 제6강 (2021-09-27) 함수와 모듈

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/06-20210927.pdf)

---

### 제7강 (2021-09-29) 예외 처리

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/07-20210929.pdf)

---

### 제8강 (2021-10-06) 정규표현식 (1)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/08-20211006.pdf)

[Slides: Text Processing by Dan Jurafsky](https://web.stanford.edu/~jurafsky/slp3/slides/2_TextProc_Mar_25_2021.pdf)


#### 참고 자료 
+ [SLP3: Ch. 2 Regular Expressions, Text Normalization, and Edit Distance](https://web.stanford.edu/~jurafsky/slp3/2.pdf)
+ [RegExr: Learn, Build, & Test RegEx](https://regexr.com/)

---

### 제9강 (2021-10-13) 정규표현식 (2)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/09-20211013.pdf)

#### 참고 자료

+ [ELIZA—a computer program for the study of natural language communication between man and machine](https://dl.acm.org/doi/10.1145/365153.365168)

---

### 제10강 (2021-10-18) 파일 처리 (1)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/10-20211018.pdf)

#### 실습 코드

https://colab.research.google.com/drive/1Wd5gP-zEMfACWaQ4fH8GcjMwRlVzC6Rq

---

### 제11강 (2021-10-20) 파일 처리 (2)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/11-20211020.pdf)

#### 참고 자료

+ [Project Gutenberg: Free eBooks](https://www.gutenberg.org/)

---

### 제12강 (2021-10-25) ELIZA 개발 관련 토의

---

### 제13강 (2021-10-27) 벡터, 통계, 데이터 시각화 (1)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/13-20211027.pdf)

#### 참고 자료
+ [밑바닥부터 시작하는 데이터 사이언스 (2판)](https://github.com/insightbook/Data-Science-from-Scratch)

---

### 제14강 (2021-11-01) 벡터, 통계, 데이터 시각화 (2)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/14-20211101.pdf)

---

### 제15강 (2021-11-03) N그램 언어 모형 (1)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/15-20211103.pdf)

#### 참고 자료

+ [SLP3: Ch. 3 N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
+ [That can be my next tweet!](https://yes.thatcan.be/my/next/tweet/)

---

### 제16강 (2021-11-08) N그램 언어 모형 (2)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/16-20211108.pdf)

#### 실습 코드

https://colab.research.google.com/drive/1XFkZApol9a8fbHHqHSybQ8BMDF6FEscL

#### 데이터

+ [The Berkeley Restaurant Project (BeRP) Transcripts](https://github.com/wooters/berp-trans)
+ [NLTK :: Sample usage for corpus](https://www.nltk.org/howto/corpus.html)

---

### 제17강 (2021-11-10) N그램 언어 모형 (3)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/17-20211110.pdf)

---

### 제18강 (2021-11-15) 단순 베이즈 분류기와 감정분석 (1)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/18-20211115.pdf)

#### 참고 자료

+ [SLP3: Ch. 4 Naive Bayes and Sentiment Classification](https://web.stanford.edu/~jurafsky/slp3/4.pdf)

---

### 제19강 (2021-11-17) 단순 베이즈 분류기와 감정분석 (2)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/19-20211117.pdf)

#### 실습 코드

https://colab.research.google.com/drive/1C8lM22-5ILMCH0CemzXKBCWXrHyc2yIJ?usp=sharing

---

### 제20강 (2021-11-22) 로지스틱 회귀분석 (1)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/20-20211122.pdf)

#### 참고 자료

+ [SLP3: Ch.5 Logistic Regression](https://web.stanford.edu/~jurafsky/slp3/5.pdf)

---

### 제21강 (2021-11-24) 로지스틱 회귀분석 (2)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/21-20211124.pdf)

#### 실습 코드

https://colab.research.google.com/drive/19PcTY3eEm-Yy0NPiCIir-0M-6Uvu4K4l?usp=sharing

#### 데이터

+ [IMDb-Review-Analysis](https://github.com/LawrenceDuan/IMDb-Review-Analysis)
+ [VADER-Sentiment-Analysis](https://github.com/cjhutto/vaderSentiment)

---

### 제22강 (2021-11-29) 로지스틱 회귀분석 (3)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/22-20211129.pdf)

#### 실습 코드

https://colab.research.google.com/drive/1AEUWk9MyA1PI8llZ7zVJD1kRqkyqxl_G?usp=sharing

---

### 제23강 (2021-12-01) 벡터 의미론 (1)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/23-20211201.pdf)

#### 실습 코드

https://colab.research.google.com/drive/1bBg_CcZduJiFS7DVTMQxg0iPgMyqodZT?usp=sharing

#### 참고 자료

+ [SLP3: Ch. 6 Vector Semantics and Embeddings](https://web.stanford.edu/~jurafsky/slp3/6.pdf)

---

### 제24강 (2021-12-08) 벡터 의미론 (2)

#### 슬라이드

[파일 링크](https://github.com/suzisuti/lecture/blob/master/2021/LC/slides/24-20211208.pdf)

#### 실습 코드

https://colab.research.google.com/drive/1FxanqyGrBVHfFl77XQPrrYyFuxCkT6Ao?usp=sharing
