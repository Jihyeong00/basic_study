"""
주소록을 관리하는 프로그램
"""


def add_address(book):
    name = input("추가할 사용자 이름을 입력해주세요. : ")
    phone = input("사용자의 전화번호를 입력해주세요. : ")
    address = input("사용자의 주소를 입력해주세요. : ")
    book[name] = {"phone": phone, "address": address}
    return book


if __name__ == "__main__":
    address_book = {}
    print()
