#두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
num =[]
for i in range(10):
    number = int(input())
    remain = number%42
    num.append(remain)

set_num =set(num)  #집합으로 중복되는 숫자를 제거해줌  > 그럼 모두 서로다른 값이라는 뜻이므로 리스트의 개수를 출력하면 된다
print(len(set_num))



