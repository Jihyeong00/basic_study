import random as r

random_operator = r.choice(["+", "-", "*", "/", "%"])

first_num = r.randint(1, 99)
second_num = r.randint(1, 99)

answer = 0

if random_operator == "+":
    answer = first_num + second_num
elif random_operator == "-":
    answer = first_num - second_num
elif random_operator == "*":
    answer = first_num * second_num
elif random_operator == "/":
    answer = first_num / second_num
elif random_operator == "%":
    answer = first_num % second_num

while int(input(f"{first_num} {random_operator} {second_num} = ?: ")) == answer:
    print("틀렸습니다. 다시 입력해주세요")


print("정답입니다.")