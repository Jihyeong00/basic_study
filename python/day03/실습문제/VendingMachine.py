# 요구사항
# ex)
# input(투입한 돈: 5000)
# input(물건값: 2650)

# output(거스름돈: 2350)
# output(500원 동전의 갯수: 4)
# output(100원 동전의 갯수: 3)
# output(10원 동전의 갯수: 5)

input_money = int(input("투입한 돈: "))
product_price = int(input("물건값: "))


# 거스름 돈 구하기 함수
def get_change_coin(money, price):
    remainder_money = money - price
    coin_500 = remainder_money // 500
    coin_500_remainder = remainder_money % 500
    coin_100 = coin_500_remainder // 100
    coin_10 = coin_500_remainder % 100 // 10

    print("거스름 돈: " + str(remainder_money))
    print("500원 동전의 갯수: " + str(coin_500))
    print("100원 동전의 갯수: " + str(coin_100))
    print("10원 동전의 갯수: " + str(coin_10))


get_change_coin(input_money, product_price)




