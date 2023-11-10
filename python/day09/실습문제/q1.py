"""
사용자에게 영어 문자열을 입력을 받고 그 중 모음의 갯수가 몇개인지 출력을 하는 프로그램
"""

VOWELS = ["a", 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def read_text():
    return input("영어문자열을 입력해주세요")


def get_vowels_count(text):
    count = 0
    for t in text:
        if t in VOWELS:
            count += 1
    return count


def get_consonant_count(text):
    count = 0
    for t in text:
        if t not in VOWELS:
            count += 1
    return count

def check_vowels_result(text, vowel_count):
    print(f"입력한 문자는 {text}이고 모음의 갯수는 {vowel_count} 입니다. ")



def check_vowels_result(text, vowel_count, consonant_count):
    print(f"입력한 문자는 {text}이고 모음의 갯수는 {vowel_count}, 자음의 갯수는 {consonant_count} 입니다. ")


text = read_text()
vowel_number = get_vowels_count(text)
consonant_number = get_consonant_count(text)

check_vowels_result(text, vowel_number, consonant_number)


