"""
영어 문자열을 입력받아 그중에서 모음의 개수를 출력
"""


def readText():
    return input("영어 문자열을 입력하세요")

def countVowel (text):
    cnt = 0
    for t in text:
        if t in ['a', 'i', 'o', 'e', 'u']:
            cnt += 1

    return cnt

text = readText()
number = countVowel(text)

print(f"입력한 문자열 {text}에는 모음이 총 {number}개 있습니다.")