my_dict = {}


def calendar_manager_run():
    while True:
        date = input("날짜를 입력하시오: ")
        if date == "q": break
        work = input("일정을 입력하시오: ")
        if date not in my_dict:
            my_dict[date] = work
        else:
            print("이미 예약된 일정이 있습니다.")

    manager_print_work_list()


def manager_print_work_list():
    for val in my_dict:
        print(f"{val}의 일정은 {my_dict[val]}입니다.")


if __name__ == "__main__":
    calendar_manager_run()
