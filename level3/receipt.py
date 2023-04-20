# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

receipt_total_price = int(input())
numberOf_items_purchased = int(input())
total_price_result = 0
for i in range(numberOf_items_purchased):
    item_price,item_number = map(int,input().split( ))
    total_price_result += item_price*item_number

if receipt_total_price == total_price_result:
    print("Yes")
else:
    print("No")


