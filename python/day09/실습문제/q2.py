import random


def lotto_machin ():
    winning_number = []
    while len(winning_number) < 6:
        random_number = random.randint(1, 45)
        if random_number not in winning_number:
            winning_number.append(random_number)

    return winning_number

print(lotto_machin())