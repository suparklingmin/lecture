# -*- coding: utf-8 -*-
# title: try.py
# course: 언어와 컴퓨터
# author: 박수지
# date created: 2018-10-11
# description: try-except 문으로 예외 처리하기

#############################
'''0. 일단 함수를 만든다.'''
def myint(string):
    return int(string)

'''한 행씩 실행시켜 보면서 다양한 오류의 유형을 살펴보자.'''
myint(42)
myint('42')
myint('4.2') # ValueError
myint([42]) # TypeError
myint('42')) # SyntaxError

#############################
'''1. 예외의 유형에 따라 다르게 처리할 수 있다.'''
def myint(string):
    try:
        return int(string)
    except ValueError:
        print('잘못된 값입니다.')
    except TypeError:
        print('자료형이 잘못되었습니다.')
    except SyntaxError:
    	print('문법이 잘못되었습니다.')
    finally:
        print('어쨌든 수고하셨습니다.')

'''except 문에 사용할 수 없는 오류의 유형은 무엇인가?'''
myint(42)
myint('42')
myint('4.2')
myint([42])
myint('42'))

'''finally 문의 스위트가 언제 실행되는지 살펴보자.'''
myint(42)
myint('42')
myint('4.2')
myint([42])

#############################
'''3. finally 문이 없어도 try/except 문은 작동한다.'''
def myint(string):
    try:
        return int(string)
    except ValueError:
        print('잘못된 값입니다.')
    except TypeError:
        print('자료형이 잘못되었습니다.')
    print('어쨌든 수고하셨습니다.')

'''2.의 실행 결과와 다른 점을 살펴보자.'''
myint(42)
myint('42')
myint('4.2') # ValueError
myint([42]) # TypeError

#############################
'''4. 오류의 유형을 따지기 귀찮다.'''
def myint(string):
    try:
        return int(string)
    except:
        print('무엇인지는 몰라도 오류가 발생했습니다.')

myint(42)
myint('42')
myint('4.2') # ValueError
myint([42]) # TypeError
