# 언어와 컴퓨터 (100.130)
서울대학교 언어학과, 2018학년도 2학기

+ 강의자: 박수지(mam3b at snu_ac_kr)
+ 목표: 이 과목은 컴퓨터언어학을 위한 기초 과정으로, 문자로 이루어진 텍스트 처리를 중심으로 인간의 언어를 컴퓨터에서 구현하는 과정을 배운다. 강좌는 크게 두 부분으로 이루어져 있다. 중간고사 이전에는 대량의 텍스트를 자동으로 처리할 수 있도록 Python 프로그램을 사용하는 방법을 익히며, 이후에는 자연언어 처리에 필요한 통계 모형에 관하여 학습한다.
+ 교재
  - Jurafsky and Martin. (forthcoming). Speech and Language Processing (3rd ed. draft) https://web.stanford.edu/~jurafsky/slp3/
  - 조엘 그루스 지음. 박은정·김한결·하성주 옮김. (2016). 《밑바닥부터 시작하는 데이터 과학: 데이터 분석을 위한 파이썬 프로그래밍과 수학·통계 기초》. 인사이트.
+ 기타 참고 자료
  - [Automating the boring stuff](https://automatetheboringstuff.com)
  - [Think Python (2nd Edition)](http://greenteapress.com/wp/think-python-2e/)
  - [씽크 파이썬](https://thebook.io/006878/)
  - [파이썬 자습서](https://docs.python.org/ko/3/tutorial/index.html)


## 수업 일정 및 자료

### 제1강 (2018-09-03) 강의 소개

### 제2강 (2018-09-05) 시작하기 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/02-20180905.pdf))
강좌의 목표, 파이썬 인터프리터, 산술 연산, 오류 메시지
#### 코드
+ [arith.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/arith.py)
+ [print_arith.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/print_arith.py)
+ [print_hello.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/print_hello.py)
#### 파이썬 인터프리터 사용하기
##### 웹
+ [repl.it](https://repl.it)
+ [Python Tutor](http://pythontutor.com)
##### 모바일
+ [QPython3 (안드로이드)](https://play.google.com/store/apps/details?id=org.qpython.qpy3)
+ [Pydroid 3 (안드로이드)](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)
+ [Pythonista 3 (iOS)](https://itunes.apple.com/kr/app/pythonista-3/id1085978097?mt=8)

### 제3강 (2018-09-10) 기본 자료형: 수와 문자열 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/03-20180910.pdf))
#### 과제
+ \[숙제02] 파이썬 기본 개념 연습
  - https://automatetheboringstuff.com/chapter1/ 연습문제

### 제4강 (2018-09-12) 반복 가능한 자료형 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/04-20180912.pdf))
객체, 리스트, 튜플, 범위, 딕셔너리
#### 코드
+ [count_char.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/count_char.py)
+ [sort_words.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/sort_words.py)
#### 도구
+ [부동소수점 변환기](https://www.exploringbinary.com/floating-point-converter/)
+ [리스트 복사 과정 시각화](http://pythontutor.com)

### 제5강 (2018-09-17) 조건문 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/05-20180917.pdf))
복합문, if, else, elif 키워드
#### 코드
+ [cold_or_not.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/cold_or_not.py)
+ [cold_or_hot.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/cold_or_hot.py)
+ [cold_or_mild_or_hot.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/cold_or_mild_or_hot.py)
+ [multi3.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/multi3.py)
+ [password.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/password.py)
+ [fridge.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/fridge.py)
+ [arith_test.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/arith_test.py)
#### 과제
+ \[숙제03] 리스트 및 조건문 연습
  - https://automatetheboringstuff.com/chapter2/ 연습문제
  - https://automatetheboringstuff.com/chapter4/ 연습문제

### 제6강 (2018-09-19) 반복문 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/06-20180919.pdf))
복합문, while, for, break, pass 키워드
#### 코드
+ [20180919-loop.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/20180919-loop.py)
+ [snooze.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/snooze.py)
#### 과제
+ [\[숙제04\] 프로그래밍 연습](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw04.pdf)
+ [\[숙제04심화\] 3-6-9 게임](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw04adv.pdf)

### 제7강 (2018-10-01) 모듈과 함수 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/07-20181001.pdf))
#### 코드
+ [word_freq_functions.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/word_freq_functions.py)
#### 과제
+ [\[숙제05\] 함수 정의 연습](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw05.pdf)

### 제8강 (2018-10-08) 파일 처리  ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/08-20181008.pdf))
#### 읽기
+ [Dive into Python 3: Chapter 11. Files](https://juehan.github.io/DiveIntoPython3_Korean_Translation/files.html)
+ [씽크 파이썬: 9장. 사례 연구: 워드 플레이](https://thebook.io/006878/ch09/)
#### 과제
+ [\[숙제06\] 파일 처리 연습](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw06.pdf)
  - 자료: [현대 국어 사용 빈도 조사 결과 파일(텍스트 파일)](http://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=46&etc_seq=61) [데이터 proper_nouns.txt](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/proper_nouns.txt)
  - 참고: [딕셔너리 사용하기](https://dojang.io/mod/page/view.php?id=1003)

### 제9강 (2018-10-10) 문자 인코딩 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/09-20181010.pdf))
#### 읽기
+ [국어 정보화의 방향: 문자 코드를 중심으로](http://www.korean.go.kr/nkview/nklife/2015_2/25_0205.pdf)
+ [‘설믜를 설믜라 못 부르는’ 김설믜씨 “제 이름을 지켜주세요”](http://www.hani.co.kr/arti/society/society_general/864914.html)

### 제10강 (2018-10-17) 한글 처리 모듈 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/10-20181017.pdf))
try 문, 한글 음절 분해, 옛한글 자모 조합
#### 읽기
+ [파이썬 자습서 8. 에러와 예외](https://docs.python.org/ko/3/tutorial/errors.html)
#### 코드
+ [try.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/try.py)
+ [hangul.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/hangul.py)
#### 옛한글 지원 글꼴
+ [본고딕(Source Han Sans)](https://github.com/adobe-fonts/source-han-sans/blob/master/README-KR.md)
+ [본명조(Source Hans Serif)](https://github.com/adobe-fonts/source-han-serif/blob/master/README-KR.md)
+ [나눔옛한글](https://hangeul.naver.com/2014/archaicword)
#### 과제
+ [\[숙제07\] 한글 처리 모듈 확장](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw07.pdf)
+ [\[숙제07심화\] 옛한글 입력 방법 추가](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw07adv.pdf)

### 중간고사

### 제11강 (2018-10-29) 텍스트 처리 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/11-20181029.pdf))
정규표현식, 코퍼스, 단어 토큰화, 단어 정제, 문장 분리
#### 코드
+ [maxmatch.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/maxmatch.py)
+ [decision_tree.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/decision_tree.py)
#### 기타
+ [형태소 깎는 노인: 국어사 자료를 위한 형태분석 보조기](http://www.ndsl.kr/ndsl/search/detail/article/articleSearchResultDetail.do?cn=NPAP12638918) — MaxMatch와 비슷한 방법으로 형태소 분리하기
+ [단어 임베딩과 음성적 유사도를 이용한 트위터 ‘서치 방지 단어’ 의 자동 예측](http://www.ndsl.kr/ndsl/search/detail/article/articleSearchResultDetail.do?cn=NPAP12638863) — 최소 편집 거리로 음성적 유사도 측정하기


### 제12강 (2018-10-31) 정규표현식 실습 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/12-20181031.pdf))
re 모듈, ELIZA
#### 코드
+ [reg_exp.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/reg_exp.py)
+ [eliza.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/eliza.py)
#### 읽기
+ [ELIZA: a computer program for the study of natural language communication between man and machine](http://doi.org/10.1145/365153.365168)
#### 도구
+ 정규표현식 테스트 [RegExr: Learn, Build, & Test RegEx](https://regexr.com)
+ 파이썬 라이브러리 [NLTK: Natural Language Toolkit](http://www.nltk.org)
+ 파이썬 라이브러리 [KoNLPy: 파이썬 한국어 NLP](http://konlpy.org/ko/latest/)
#### 과제
+ [\[숙제09\] ELIZA 완성하기 (조별)](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw09.pdf)
  - 자료: [eliza.txt](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/eliza.txt)
+ [\[숙제09심화\] 최소 편집 거리 알고리듬 구현하기](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw09adv.pdf)


### 제13강 (2018-11-07) 벡터, 통계, 데이터 시각화 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/13-20181107.pdf))
밑바닥부터 시작하는 데이터 과학 3장–8장.
#### 코드
+ [vectors.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/vectors.py)
+ [statistics.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/statistics.py)
#### 과제
+ [\[숙제10\] NumPy 및 SciPy 연습](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw10.pdf)
+ [\[숙제10심화\] 트위터 사용자 데이터 분석](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw10adv.pdf)
  - 자료: [tweets.txt](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/tweets.txt)
  - [해설](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw10adv_solutions.pdf)
#### 도구
+ [NumPy](http://www.numpy.org)
+ [SciPy](https://www.scipy.org)

### 제14강 (2018-11-12) n-그램 언어 모형 (1) ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/14-20181112.pdf))

### 제15강 (2018-11-14) n-그램 언어 모형 (2) ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/15-20181114.pdf))
#### 코드
+ 문장 생성 [generate.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/generate.py)
+ “영어스러운 단어 생성” [ngrams.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/ngrams.py)
   - 자료: [literary.txt](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/literary.txt) https://en.oxforddictionaries.com/explore/literary-words
#### 과제
+ [\[숙제11\] n-그램 언어 모형](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw11.pdf)


### 제16강 (2018-11-19) 단순 베이즈 분류기와 감정분석 (1) ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/16-20181119.pdf))

### 제17–18강 (2018-11-21,26) 단순 베이즈 분류기와 감정분석 (2-3) ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/17-20181121.pdf))
#### 코드
+ 영화평 분류 [naivebayes_practice.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/naivebayes_practice.py)
  - 자료: [reviews.txt](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/reviews.txt) 
    = 참조: [꼬꼬마 형태소 분석기: 품사 태그표](http://kkma.snu.ac.kr/documents/index.jsp?doc=postag)
#### 과제
+ [\[숙제12\] 단순 베이즈 분류기를 사용한 당시(唐詩)의 감정 분류](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw12.pdf)
  - 자료: [Sentiment lexicon for classical Chinese poetry](https://www.cl.uni-heidelberg.de/~hou/resources.mhtml) [데이터 poems.txt](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/poems.txt)


### 제19강 (2018-11-28) scikit-learn과 NLTK를 사용한 기계학습 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/19-20181128.pdf))
#### 코드
+ [naivebayes_nltk.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/naivebayes_nltk.py)
+ [naivebayes_sklearn.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/naivebayes_sklearn.py)
#### 읽기
+ [NLTK: Learning to Classify Text](http://www.nltk.org/book/ch06.html)
+ [scikit-learn: Working With Text Data](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)
#### 도구
+ [일부 환경에서 scikit-learn 설치 후 NumPy와 SciPy를 재설치하는 방법](https://code.i-harness.com/ko-kr/q/232f672)
#### 과제
+ [\[숙제13\] 악성 트윗 분류기 개발하기 (조별)](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw13.pdf)
  - 읽기: [Automated Hate Speech Detection and the Problem of Offensive Language](https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665)
  - 자료: https://github.com/t-davidson/hate-speech-and-offensive-language [데이터 파일 train.txt]([데이터](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/train.txt)


### 제20강 (2018-12-03) 로지스틱 회귀분석 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/20-20181203.pdf))

### 기말고사
