input_sec = int(input("시간을 구할 초를 입력해주세요 : "))

# 요구사항
# 클라이언트에게 값을 입력을 받고 해당하는 시간에 맞게 다음 결과 값으로 출력하시오.
# ex)
# input(9020)
# output(입력한 9020초는 2시간 30분 20초 입니다.)


def time_helper(number):
    # 시간 구하기
    hour = number // (60 * 60)
    # 시간 이외에 초 구하기
    hour_remain = number % (60 * 60)
    # 분 구하기
    minute = hour_remain // 60
    # 나머지 초 구하기
    sec = hour_remain % 60
    print("입력한 " + str(sec) + "초는 " + str(hour) + "시간" + str(minute) + "분" + str(sec) + "초 입니다.")


time_helper(input_sec)


