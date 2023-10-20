import random


#  2자리의 숫자를 받아 랜덤한 숫자와 비교한 후 맞은 숫자에 따라서 상금이 지급되는 프로그램


def make_random_number():
    first_number = random.randint(0, 9)
    while True:
        second_number = random.randint(0, 9)
        if first_number != second_number:
            break

    return [first_number, second_number]


def check_number(text1, text2):
    result = ""
    if f"{text1[0]}${text1[1]}" == text2:
        result = "1등입니다."
    else:
        for i in range(len(text1)):
            if text1[i] == text2[i]: result = "2등입니다"

    if result == "": return "3등입니다."
    return result


random_str = make_random_number()

input_text = input("중복되지 않은 2자리 숫자를 입력해주세요 : ")

print(random_str)
print(check_number(random_str, input_text))

