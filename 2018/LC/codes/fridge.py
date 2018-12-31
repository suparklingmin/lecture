# -*- coding: utf-8 -*-
fridge = ['주스', '두부', '요거트', '요거트']
food = input('찾는 것을 입력하세요: ')
if food in fridge:
    fridge.remove(food)
    print('냉장고에 남은 것: {}'.format(fridge))
else:
    print('냉장고에 없습니다.')
