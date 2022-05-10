# n = input().split()
# print(n)  > 리스트 형태로 반환됨

import sys
stack =[]

n = int(sys.stdin.readline())

for i in range(n):
    x = sys.stdin.readline().split()
    if x[0] == "push" :
        stack.append(x[1]) # 문자말고 정수를 넣어줌
    elif x[0] == "pop":
        if len(stack) <= 0 :
            print(-1)
        else:
            print(stack.pop())
    elif x[0] == "size":
        print(len(stack))
    elif x[0] == "empty":
        if len(stack) <= 0:
            print(1)
        else:
            print(0)
    elif x[0] == "top":
        if len(stack) <= 0 :
            print(-1)
        else:
            print(stack[-1])

    
