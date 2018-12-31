# -*- coding: utf-8 -*-
# title: eliza.py
# course: Language and Computer
# author(s): Suzi Park
# date created: 2018-10-29
# description: ELIZA

import re, random

def respond(message):
    # preprocessing
    message = message.upper()
    message = re.sub(r'\s+', ' ', message)
    
    # generalization
    if re.match(r".*\bALL\b.*", message):
        return 'IN WHAT WAY'
    elif re.match(r".*\bALWAYS\b.*", message):
        return 'CAN YOU THINK OF A SPECIFIC EXAMPLE'
    
    # "I'm sad"
    match = re.match(r".*\bI(?: AM|'M) (DEPRESSED|SAD|SICK|UNHAPPY)\b.*", message)
    if match:
        sad = match.group(1)
        responses = [
            f"I AM SORRY TO HEAR THAT YOU ARE {sad}",
            f"WHY DO YOU THINK YOU ARE {sad}",
        ]
        return random.choice(responses)
    
    # "my"
    match = re.match(r".*\bMY (.*)", message)
    if match:
        response = f'YOUR {match.group(1)}'
        response = re.sub(r'\bME\b', 'YOU', response)
        response = re.sub(r'\bMY(SELF)?\b', r'YOUR\1', response)
        return response
    
    # no keyword
    responses = [
        "PLEASE GO ON",
        "WHAT DOES THAT SUGGEST TO YOU",
        "I'M NOT SURE I UNDERSTAND YOU FULLY"
    ]
    return random.choice(responses)


if __name__ == '__main__':
    print('PLEASE TELL ME YOUR PROBLEM')
    message = input('> ')
    while message not in ('', 'quit'):
        print(respond(message))
        message = input('> ')
    
    print('GOODBYE')
