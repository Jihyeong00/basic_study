import random as r

"""
리스트를 입력을 받아 해당 리스트의 원소 값 중 최고 값을 구하는 프로그램
"""


def make_random():
    return r.randint(1, 99)


def make_random_list(count):
    random_list = []
    for _ in range(count):
        random_list.append(make_random())
    return random_list


def get_max_value_in_list(target_list):
    max_value = target_list[0]
    for value in target_list:
        if max_value < value:
            max_value = value
    return max_value


mock_data = [[10, 20, 30, 40, 50, 60], [15, 25, 35, 45, 55, 65]]

for i in mock_data:
    print(get_max_value_in_list(i))

for i in range(10):
    print(get_max_value_in_list(make_random_list(10)))
