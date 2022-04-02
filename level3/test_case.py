#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
#각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다.
t = int(input())

for x in range(1,t+1) :
    a,b = map(int,input().split())
    print(f"Case #{x}: {a+b}")