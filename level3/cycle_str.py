n = input() #input()기본값은 문자열로 들어옴
num = n 
cnt = 0

while 1 :
    if len(num) == 1:
        num= "0"+num
    plus = str(int(num[0]) +int(num[1])) #첫번째 값과 두번째값을 더함
    num = num[-1] + plus[-1]  #n의 오른쪽자리수와 합한값의 오른쪽자리수를 문자열로 합함(이어붙임)
    cnt +=1
    if num ==n :
        print(cnt)
        break