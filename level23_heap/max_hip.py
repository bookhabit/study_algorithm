# # 내가 짠 코드 시간초과
# from sys import stdin

# heap = []
# result = []

# num = int(stdin.readline())

# for i in range(num):
#     x = int(stdin.readline())
#     if x > 0 :
#         heap.append(x)
#     if x == 0 :
#         try:
#             print(max(heap))
#             heap.remove(max(heap))
#         except:
#             print(0)

# 구글링
import heapq
from sys import stdin

n = int(stdin.readline())
heap =[]

for _ in range(n):
    num = int(stdin.readline())

    if num == 0:
        if heap:  # 배열이 비어있으면 False가 됨
            print(heapq.heappop(heap)[1])
        else:
            print("0")
    else:
        heapq.heappush(heap,(-num,num))