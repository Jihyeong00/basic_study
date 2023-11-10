import random
"""
1에서 100사이의 열개 짜리 롯도 숫자를 숫자 중복 x 짝수 x 문자 5번 출력
"""

import random


def lotto_machin ():
    winning_number = []
    while len(winning_number) < 10:
        random_number = random.randint(1, 100)
        if random_number not in winning_number and random_number % 2 != 0:
            winning_number.append(random_number)

    return winning_number

def print_lotto():
    for i in range(5):
        print(str(i+1) + "회차의 로또의 결과입니다 : "+ str(lotto_machin()))

print_lotto()