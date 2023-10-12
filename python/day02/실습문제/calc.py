# 요구사항 3번, 3개 숫자를 사용자로부터 입력받아 합과 평균값 출력하기

sum_result = 0

# 질문할 횟수
answer_count = 3

for i in range(answer_count):
    sum_result += int(input(str(i + 1) + "번째 숫자를 입력 해주세요. "))

print("평균 값은 : " + str(sum_result / 3))
