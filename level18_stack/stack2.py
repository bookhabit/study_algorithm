#정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 클래스 말고 함수로 구현해봄

stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) <= 0 :
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) <= 0 :
        print(1)
    else:
        print(0)

def top():
    if len(stack) <= 0 :
        print(-1)
    else:
        print(stack[-1])


n = int(input())

for i in range(n):
    x = input()  # 명령어 입력
    # push라는 문자열이 x에 포함되어 있다면
    if "push" in x :  # push 일 경우
# 공백을 구분으로 뒤에문자 숫자를 push함수에 입력값을 전달해줘야 한다
        chr,num = x.split(" ")
        num = int(num)
        #print(chr,num)
        push(num)
    elif x == "pop":
        pop()
    elif x == "size":
        size()
    elif x == "empty":
        empty()
    elif x == "top":
        top()
# 입력받은 문자열을 매개변수로 넘겨줘서 조건문으로 문자열 비교해서 함수를 실행시킴

    
