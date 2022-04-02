#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
#각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력
t = int(input())

for x in range(1,t+1) :
    a,b = map(int,input().split())
     # "Case #x: A + B = C" 
    print(f"Case #{x}: {a} + {b} = {a+b}")