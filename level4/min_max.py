#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
n = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in range(n) :
    if max < numbers[i] :
        max = numbers[i]
    if min > numbers[i] :
        min = numbers[i]

print(min,max)
# n = int(input())
# max =0
# min =0
#arr =list(map(int,input().split(" ")))
# min = arr[0]
# for i in arr :
#     if max < arr[i]:
#         max = arr[i]
#     if min > arr[i] :
#         min = arr[i]
# print(min,max)