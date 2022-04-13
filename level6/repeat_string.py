t = input()

p =""
for i in range(int(t)): #테스트 케이스
    r,s = input().split() # r은 반복횟수 s는 문자열
    for j in s :
        p += (j*int(r))
    print(p)
    p= ""
