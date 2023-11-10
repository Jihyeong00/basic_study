# 3명이 학생의 이름, 국, 영, 수 점수를 입력 받아 각 학생들의 총점 평균과 전체 학생의 총점 평균을 구하는 프로그램

def get_student_info():
    student_info = []
    student_info.append(input("학생 이름: "))
    student_info.append(int(input("국어 점수: ")))
    student_info.append(int(input("영어 점수: ")))
    student_info.append(int(input("수학 점수: ")))
    student_info.append(student_info[1] + student_info[2] + student_info[3])
    student_info.append(int(student_info[4] / 3))
    return student_info


def get_student_list(items):
    print("=================================================")
    print(f"%10s%3s%3s%3s%5s%5s" % ("성명", "국어", "영어", "수학", "총점", "평균"))

    items_length = len(items)

    kor_sum = 0
    eng_sum = 0
    math_sum = 0

    for i in range(items_length):
        kor_sum += items[i][1]
        eng_sum += items[i][2]
        math_sum += items[i][3]
        print(f"%10s%3s%3s%3s%5s%5s" % (
            items[i][0], str(items[i][1]), str(items[i][2]), str(items[i][3]), str(items[i][4]), str(items[i][5])))

    print("=================================================")

    kor_avg = kor_sum / items_length
    eng_avg = eng_sum / items_length
    math_avg = math_sum / items_length

    print(f"%s\t%s\t%s\t%s" % (
        "총점/평균",
        str(kor_sum) + "/" + str(kor_avg), str(eng_sum) + "/" + str(eng_avg), str(math_sum) + "/" + str(math_avg)))


student_list = []

while True:
    select = int(input("메뉴 선택\n학생 추가: 1\n목록 보기: 2 :"))

    if select == 1:
        student_list.append(get_student_info())
    elif select == 2:
        get_student_list(student_list)
        break
