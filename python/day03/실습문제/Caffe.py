# 요구사항
# 클라이언트에게 각각의 커피 종류마다 구매한 갯수 값을 입력을 받고 해당 커피의 값을 출력하시오
# ex)
# input(10)
# input(20)
# input(30)
# output(총 매출은 185000 입니다.)

# 커피 각 종류의 갯수를 입력받기
ame_count = int(input("아메리카노 판매 개수: "))
latte_count = int(input("카페라떼 판매 개수: "))
chino_count = int(input("카푸치노 판매 개수: "))

# 커피 단가의 설정하기
AME_PRICE = 2000
LATTE_PRICE = 3000
CHINO_PRICE = 3500


def get_sales(ame, latte, chino):
    """
    :param ame: 아메리카노의 판매 갯수를 입력을 받습니다.
    :param latte: 카페라떼의 판매 갯수를 입력을 받습니다.
    :param chino: 카푸치노의 판매 갯수를 입력을 받습니다.
    :return:
    """
    ame_price = ame * AME_PRICE
    latte_price = latte * LATTE_PRICE
    chino_price = chino * CHINO_PRICE

    # 전체 합을 구합니다.
    sum_price = ame_price + latte_price + chino_price
    return sum_price


print("총 매출은" + str(get_sales(ame_count, latte_count, chino_count)) + " 입니다.")

