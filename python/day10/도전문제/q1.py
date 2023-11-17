import random as r


def make_number ():
    first_num = r.randint(1, 99)
    second_num = r.randint(1, 99)
    return [first_num, second_num]


def make_random_operator ():
    [first_num, second_num] = make_number()
    random_operator = r.choice(["+", "-", "*", "/", "%"])
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

    return [first_num, second_num, random_operator, answer]


def play_game():
    [first_num, second_num, random_operator, answer] = make_random_operator()
    print(answer)
    while int(input(f"{first_num} {random_operator} {second_num} = ?: ")) != answer:
        print("틀렸습니다. 다시 입력해주세요")
    print("정답입니다.")

play_game()