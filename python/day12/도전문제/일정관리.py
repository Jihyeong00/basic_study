mydict = {}

while True:
    date = input("날짜를 입력하시오 : ")
    if date == "q":
        break
    job = input("일정을 입력하시오")
    if date in mydict:
        mydict[date].append(job)
    else:
        mydict[date] = [job]

print(mydict)