#훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
#첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)
# h,m = map(int,input().split())
# c = int(input())
# if h < 23 :
#     if  m+c >= 60 :
#         h = h+1
#         m = (m+c)-60
#         print(h,m)
#     elif  m+c < 60 :
#         m = m+c
#         print(h,m)
# #elif h==23 and m+c >= 60 :
# else :
#     if  m+c >= 60 :
#         h = h+1
#         m = (m+c)-60
#         print(h,m)
#     elif  m+c < 60 :
#         m = m+c
#         print(h,m)
#     h = 0
#     m = (m+c)-60
#     print(h,m)
H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)