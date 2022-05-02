# n은 동전의 종류
# n을 적절히 사용해서 그 가치의 합을 k로 만들려고 한다 
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오
# 둘째줄부터 n개의 줄에 동전의 가치 A가 오름차순으로 주어짐

# k는 동전의 종류로 만들어야 할 최종 가격
n,k = map(int,input().split())
#print(n,k)
arr = []
for i in range(n):
    coin=int(input())
    arr.append(coin)
arr.sort(reverse=True)
# print(arr)
# arr = [1,5,10,50,100,500,1000,5000,10000,50000] 동전의 종류가 배열에 담김
count =0

for coin in arr :
    count += (k//coin)      # 최종가격을 동전의 종류로 나눈다  > 몫을 count로
    k %= coin  # 최종가격을 동전의 종류로 나눈 나머지(즉, 남은 금액)> k로

print(count)