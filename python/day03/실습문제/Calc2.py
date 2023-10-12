# 요구사항
# 2개의 2자리 정수를 무작위로 생성
# 사용자에게 덧셈 결과값을 일력받아 맞으면 "정답" 틀리면 " 오답
# 사용자에게 뺄셈 결과값을 일력받아 맞으면 "정답" 틀리면 " 오답
# 사용자에게 곱셈 결과값을 일력받아 맞으면 "정답" 틀리면 " 오답
# 사용자에게 나눗셈 결과값을 일력받아 맞으면 "정답" 틀리면 " 오답

import random

# 2자리 정수 입력을 받기
first_number = random.randint(10, 99)
second_number = random.randint(10, 99)


# 전달받은 두개의 값이 같으면 정답 아니면 오답을 출력해줍니다.
def check_number(first_num, second_num):
    if first_num == second_num:
        print("정답입니다.")
    else:
        print("오답입니다.")


plus_answer = int(input(str(first_number) + " + " + str(second_number) + " = "))
check_number(first_number + second_number, plus_answer)

minus_answer = int(input(str(first_number) + " - " + str(second_number) + " = "))
check_number(first_number - second_number, minus_answer)

multiple_answer = int(input(str(first_number) + " * " + str(second_number) + " = "))
check_number(first_number * second_number, multiple_answer)

divide_answer = int(input(str(first_number) + " % " + str(second_number) + " = "))
check_number(first_number % second_number, divide_answer)


