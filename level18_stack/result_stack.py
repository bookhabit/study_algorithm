# 시간 초과로 인해 배열에 원소를 추가할 때 인덱스로 접근한다
# last in first out
# push는 append()로  pop은 그냥 pop으로 >> 파이썬 기본 리스트로 스택 구현
import sys
stack =[]

n = int(sys.stdin.readline())

for i in range(n):
    x = input()
    if "push" in x :
        chr,num = x.split(" ")
        num = int(num)
        stack.append(num)
    elif x =="pop":
        if len(stack) <= 0 :
            print(-1)
        else:
            print(stack.pop())
    elif x =="size":
        print(len(stack))
    elif x == "empty":
        if len(stack) <= 0:
            print(1)
        else:
            print(0)
    elif x == "top":
        if len(stack) <= 0 :
            print(-1)
        else:
            print(stack[-1])

