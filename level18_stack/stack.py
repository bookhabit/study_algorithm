#정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#def stack():
import sys
class stack_class :
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) <= 0 :
            print(-1)
        else:
            print(self.stack.pop())

    def size(self):
        print(len(self.stack))

    def empty(self):
        if len(self.stack) <= 0 :
            print(1)
        else:
            print(0)

    def top(self):
        if len(self.stack) <= 0 :
            print(-1)
        else:
            print(self.stack[-1])

# 스택 구현
st = stack_class()
# st.pop()
# st.push(10)
# st.push(2)
# st.empty()
# st.top()
# st.pop()
# st.top()
# st.pop()

# n = int(input()))
n = int( sys.stdin.readline())

for i in range(n):
    x = input()  # 명령어 입력
    # push라는 문자열이 x에 포함되어 있다면
    if "push" in x :  # push 일 경우
# 공백을 구분으로 뒤에문자 숫자를 push함수에 입력값을 전달해줘야 한다
        chr,num = x.split(" ")
        num = int(num)
        #print(chr,num)
        st.push(num)
    elif x == "pop":
        st.pop()
    elif x == "size":
        st.size()
    elif x == "empty":
        st.empty()
    elif x == "top":
        st.top()
# 입력받은 문자열을 매개변수로 넘겨줘서 조건문으로 문자열 비교해서 함수를 실행시킴

    
