# 윤년
# 4의배수 and  not 100의배수
year = int(input())

if year%4==0 :
    if year%100 != 0 or year%400 ==0:
        print(1)
    else:
        print(0)
else:
    print(0)
