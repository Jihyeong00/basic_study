print("입력 문자열 :")
input = "You said some winds blow forever and I didn't understand"
print(input)

str_array = input.split(' ')

delete_array = ['some', 'forever']

print("삭제 단어들 :")
print(delete_array)
for val in delete_array:
    if val in str_array:
        str_array.remove(val)
    else:
        print(val + " 없는 단어입니다.")
print("삭제 후 남은 타이틀 :")
print(str_array)

