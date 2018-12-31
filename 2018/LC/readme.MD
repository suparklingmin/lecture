# 언어와 컴퓨터 (100.130)
서울대학교 언어학과, 2018학년도 2학기

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
강좌의 목표, 파이썬 인터프리터, 산술 연산, 오류 메시지 파일
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
#### 과제
+ \[숙제01] 파이썬 환경 만들기

### 제3강 (2018-09-10) 기본 자료형: 수와 문자열 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/03-20180910.pdf))
#### 과제
+ \[숙제02] 파이썬 기본 개념 연습
  - https://automatetheboringstuff.com/chapter1/ 연습문제

### 제4강 (2018-09-12) 반복 가능한 자료형 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/04-20180912.pdf))
객체, 리스트, 튜플, 범위, 딕셔너리 파일
#### 코드
+ [count_char.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/count_char.py)
+ [sort_words.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/sort_words.py)
#### 도구
+ [부동소수점 변환기](https://www.exploringbinary.com/floating-point-converter/)
+ [리스트 복사 과정 시각화](http://pythontutor.com)

### 제5강 (2018-09-17) 조건문 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/05-20180917.pdf))
복합문, if, else, elif 키워드 파일
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
복합문, while, for, break, pass 키워드 파일
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
  - 자료: [현대 국어 사용 빈도 조사 결과 파일(텍스트 파일)](http://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=46&etc_seq=61)
  - 참고: [딕셔너리 사용하기](https://dojang.io/mod/page/view.php?id=1003)

### 제9강 (2018-10-10) 문자 인코딩 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/09-20181010.pdf))
#### 읽기
+ [국어 정보화의 방향: 문자 코드를 중심으로](http://www.korean.go.kr/nkview/nklife/2015_2/25_0205.pdf)
+ [‘설믜를 설믜라 못 부르는’ 김설믜씨 “제 이름을 지켜주세요”](http://www.hani.co.kr/arti/society/society_general/864914.html)

### 제10강 (2018-10-17) 한글 처리 모듈 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/10-20181017.pdf))
try 문, 한글 음절 분해, 옛한글 자모 조합 파일 
#### 읽기
+ [파이썬 자습서 8. 에러와 예외](https://docs.python.org/ko/3/tutorial/errors.html)
#### 코드
+ [try.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/try.py)
+ [hangul.py](https://github.com/suzisuti/lecture/blob/master/2018/LC/codes/hangul.py)
#### 과제
+ [\[숙제07\] 한글 처리 모듈 확장](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw07.pdf)
+ [\[숙제07심화\] 옛한글 입력 방법 추가](https://github.com/suzisuti/lecture/blob/master/2018/LC/hw/hw07adv.pdf)

### 중간고사

### 제11강 (2018-10-29) 텍스트 처리 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/11-20181029.pdf))

### 제12강 (2018-10-31) 정규표현식 실습 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/12-20181031.pdf))

### 제13강 (2018-11-07) 벡터, 통계, 데이터 시각화 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/13-20181107.pdf))

### 제14강 (2018-11-12) n-그램 언어 모형 (1) ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/14-20181112.pdf))

### 제15강 (2018-11-14) n-그램 언어 모형 (2) ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/15-20181114.pdf))

### 제16강 (2018-11-19) 단순 베이즈 분류기와 감정분석 (1) ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/16-20181119.pdf))

### 제17–18강 (2018-11-21,26) 단순 베이즈 분류기와 감정분석 (2-3) ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/17-20181121.pdf))

### 제19강 (2018-11-28) scikit-learn과 NLTK를 사용한 기계학습 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/19-20181128.pdf))

### 제20강 (2018-12-03) 로지스틱 회귀분석 ([슬라이드](https://github.com/suzisuti/lecture/blob/master/2018/LC/slides/20-20181203.pdf))

### 기말고사
