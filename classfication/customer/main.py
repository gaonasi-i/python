# 객체 리스트
# Customer - 2명, Gold - 2명, VIP - 1명
from classfication.customer.customer import Customer
from classfication.customer.goldcustomer import GoldCustomer
from classfication.customer.vipcustomer import VIPCustomer

Customer = [
    Customer(101, "놀부"),
    Customer(102, "팥쥐"),
    GoldCustomer(202, "흥부"),
    GoldCustomer(202, "콩쥐"),
    VIPCustomer(301,"심청", 1004)
]

print("**********구매 가격과 보너스 포인트 계산************")
for cus in Customer:
    price = 10000
    cost = cus.calc_price(price)
    print(cus.getname() + "님의 지불 금액은" + format(cost,' ,d') + "원 입니다.")

print("**********고객 정보 출력************")
# 전체 출력
for cus in Customer:
    print(cus)