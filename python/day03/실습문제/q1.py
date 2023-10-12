# 두 개의 정수를 입력 받아서 정수의 합, 차, 곱, 평균, 큰 수, 작은 수를 계산하여 화면에 출력하느 ㄴ프로그램
number1 = int(input("x: "))
number2 = int(input("y: "))

print("두 수의 합: " + str(number1 + number2))
print("두 수의 차: " + str(number1 - number2))
print("두 수의 곱: " + str(number1 * number2))
print("두 수의 평균: " + str(float((number1 + number2))/2))
print("큰수: " + str(max(number1, number2)))
print("작은수: " + str(min(number1, number2)))
