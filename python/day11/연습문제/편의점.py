"""
편의점 프로그램

상품을 추가, 감소, 가능한 프로그램입니다.

"""

initial_items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 4}


# 상품을 등록하는 함수.
def register_product(product):
    if len(product) > 50:
        print("관리하는 물품의 개수가 50개가 넘습니다.\n")
        return product

    product_name = input("등록할 물품의 이름을 입력해주세요: ")
    while is_product(product, product_name):
        product_name = input("중복된 이름입니다. 물품의 이름을 다시 입력해주세요: ")

    product_count = int(input("등록할 물품의 갯수를 입력해주세요: "))
    product[product_name] = product_count

    print(product_name + " 물품이 " + str(product_count) + "개 등록 되었습니다.\n")

    return product


# 상품의 갯수를 추가하는 함수
def is_product(product, product_name):
    return product_name in product


# 상품을 업데이트 하는 함수
def update_product(product, update_product_name, new_count):
    product[update_product_name] = new_count
    return product


# 상품의 갯수를 증가하는 함수
def increase_product_count(product):
    product_name = check_product_with_message(product, "증가시킬 상품의 이름을 알려주세요: \n")
    product_count = product[product_name] + 1
    return update_product(product, product_name, product_count)


def check_product_with_message(product, message):
    while True:
        product_name = input(message)
        if not is_product(product, product_name):
            print("해당 상품은 존재하지 않습니다.\n")
            continue
        else:
            break
    return product_name


# 상품의 개수를 감소하는 함수
def decrease_product_count(product):
    product_name = check_product_with_message(product, "감소시킬 상품의 이름을 알려주세요: \n")
    product_count = product[product_name] - 1
    if product_count <= 0:
        print("상품이 재고가 0이되어 삭제하였습니다.\n")
        delete_product(product, product_name)

    return update_product(product, product_name, product[product_name] - 1)


# 상품을 삭제하는 함수
def delete_product(product, delete_name=""):
    if delete_name == "":
        delete_name = check_product_with_message(product, "삭제할 상품의 이름을 알려주세요: \n")
    del product[delete_name]
    print("해당 " + delete_name + " 상품은 삭제 되었습니다.\n")
    return product


def print_all_product(product):
    print(product)
    for i in product:
        print(str(i) + " : " + str(product[i]) + "개 보유중 입니다.")
    print("\n")


def store(manage_product):
    while True:
        print("메뉴 : 1.신규 물품 재고 등록, 2. 특정 물품 재고량 증가, 3. 특정 물품 재고량 감소, 4.특정 물품 삭제, 5. 전체 출력")
        select_number = int(input("실행할 메뉴를 입력하세요: "))
        if select_number == 1:
            manage_product = register_product(manage_product)
        elif select_number == 2:
            manage_product = increase_product_count(manage_product)
        elif select_number == 3:
            manage_product = decrease_product_count(manage_product)
        elif select_number == 4:
            manage_product = delete_product(manage_product)
        elif select_number == 5:
            print_all_product(manage_product)
        elif select_number == 6:
            break
        else:
            print("1 ~ 6번 중에 선택하세요")


if __name__ == "__main__":
    store(initial_items)
