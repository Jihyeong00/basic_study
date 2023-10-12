# 4가지 정수를 입력받아 각 자릿수 값의 합을 출력합니다.

input_number = int(input("4자리 정수를 입력해주세요"))

ones = input_number % 10
input_number //= 10
tens = input_number % 10
input_number //= 10
hundreds_digit = input_number % 10
input_number //= 10
thousands_digit = input_number % 10

sum_result = thousands_digit + hundreds_digit + tens + ones
print(sum_result)
