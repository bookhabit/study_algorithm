a,b,c = map(int,input().split( ))

if a==b and b==c and a==c : #3개의 눈이 같은 경우
    print(10000+a*1000)
elif a==b : # 2개의 눈이 같은 경우
    print(1000+a*100)
elif a==c :
    print(1000+a*100)
elif b==c :
    print(1000+b*100)
elif a!=b and b!=c and a!=c : #3개의 눈이 모두 다를 경우
    var = [a,b,c]
    num = max(var)
    print(num*100)

