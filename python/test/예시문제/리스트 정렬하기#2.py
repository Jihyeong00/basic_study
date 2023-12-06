numbers = [9, 6, 7, 1, 8, 4, 5, 3, 2]
new_list = sorted(numbers)
# 원본 값을 유지해 줍니다.
print(numbers)
print(new_list)

reverse_list = sorted(numbers, reverse=True)
print(reverse_list)