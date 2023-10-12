#  1970년 1월 1일 이후로 현재 GMT 시간에서 시와 분만 구하는 프로그램
import time

DAY = 60 * 60 * 24
MINUTE = 60 * 60
SECOND = 60

total_sec = time.time()

get_total_sec = int(total_sec)


def gmt_time_helper(datetime):
    # 년 월 제외 시간 구하기
    sec = datetime % DAY
    # 시간 구하기
    hour = sec // MINUTE
    # 분 구하기
    minute = sec % MINUTE // SECOND
    
    return "현재시간 (GMT) : " + str(hour) + "시" + str(minute) + "분"


print(gmt_time_helper(get_total_sec))

