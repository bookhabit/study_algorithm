# x보다 작은 수를 구하라 A에서 X보다 작은 수를 모두 출력하는 프로그램
n,x = map(int,input().split())
A = list(map(int,input().split()))

for i in range(n) :
    if A[i] <  x :
        print(A[i],end= " ")



