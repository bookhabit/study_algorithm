#상수는 숫자를 거꾸로읽음  그리고 큰 수를 말함
a,b =input().split()

reversed_a = a[::-1]  #슬라이싱으로 step을 이용해 반대방향으로 문자열 넣어줌
reversed_b = b[::-1]
    
if int(reversed_a) > int(reversed_b) :
    print(int(reversed_a))
else :
    print(int(reversed_b))
