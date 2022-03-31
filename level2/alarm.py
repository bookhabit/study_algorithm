#45분 일찍 알람설정하기
H,M = map(int,input().split())
#print(H,M)
if M > 44 :
    print(H,M-45)
elif M < 45 and H > 0 :
    print(H-1,M+15)
else :
    print(23,M+15)
