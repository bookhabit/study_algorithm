#n이 주어졌을 때 n의 사이클의 길이를 구하는 방법
#1110번 정수로 풀이하는법
n = int(input())
num=n
cnt =0

while True:
    a = num//10 #몫  >첫째자리 숫자
    b = num%10 #나머지 >두번째자리 숫자
    c = (a+b) %10 # 자리수끼리 합 구하고 나머지
    num = (b*10)+c  #앞에 오른쪽자리수와  합의 가장오른쪽자리수 이어붙임 10자리수로 만들고 c는 더해서 1의자리로 만듬
    
    cnt = cnt +1
    if(num == n):
        break

print(cnt) #사이클의 수 출력