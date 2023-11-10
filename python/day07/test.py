total = []

num = int(input("입력받을 학생 수"))

top_1_score = 0
top_2_score = 0
top_3_score = 0

top_1_name = ""
top_2_name = ""
top_3_name = ""

sum = 0
avg = 0

for i in range(num):
    student = []
    name = input(str(i + 1) + "번째 학생의 이니셜")
    grade = int(input(str(i + 1) + "번째 학생의 학년"))
    score = int(input(str(i + 1) + "번째 학생의 총점"))

    sum += score

    avg = sum / num

    if grade == 1:
        if top_1_score < score:
            top_1_score = score
            top_1_name = name
    elif grade == 2:
        if top_2_score < score:
            top_2_score = score
            top_2_name = name
    elif grade == 3:
        if top_3_score < score:
            top_3_score = score
            top_3_name = name

    student.append(name)
    student.append(grade)
    student.append(score)

    total.append(student)
print(f"1학년 수석 : {top_1_name} 총점 : {top_1_score}")
print(f"2학년 수석 : {top_2_name} 총점 : {top_2_score}")
print(f"3학년 수석 : {top_3_name} 총점 : {top_3_score}")

print("총 %d명 학생들의 평점 : %.2f" % (num, avg))