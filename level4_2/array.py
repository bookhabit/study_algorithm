# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# n,x = map(int,input().split())
# arr=list(map(int,input().split()))
# for i in range(n):
#     if x > arr[i] :
#         print(arr[i], end=" ")


# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# n = int(input())
# arr = list(map(int,input().split()))
# print(min(arr),max(arr))

# n = int(input())
# numbers = list(map(int, input().split()))
# max = numbers[0]
# min = numbers[0]

# for i in range(n) :
#     if max < numbers[i] :
#         max = numbers[i]
#     if min > numbers[i] :
#         min = numbers[i]

#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# arr = []

# for i in range(9):
#     x = int(input())
#     arr.append(x)

# maxNum = max(arr)
# maxNumIndex = arr.index(maxNum)+1  # 문제에서는 0번째가 아닌 1번째 시작하기 때문
# print(maxNum) # 리스트에서 최대값 반환
# print(maxNumIndex) # 특정요소의 index반환


# 과제 안내신분?
#X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
#교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

# attendance = [i for i in range(1,31)]

# for i in range(28):
#     n = int(input())
#     attendance.remove(n)

# attendance.sort()

# for i in attendance:
#     print(i)

# 나머지
arr = []
for i in range(10):
    x = int(input())
    remain = x%42
    arr.append(remain)
print(arr)

# 중복제거 - 집합자료형으로
not_duplication_arr = set(arr)

# 중복이 없으니 모두 다른값이 들어있음 - 리스트 개수 출력
print(len(not_duplication_arr))