
n = int(input())

# 연속된 문자열은 +1 해줌 
for i in range(n):
    b = input()  #문자열을 입력받음
    s = list(b)  #받은 문자열을 list로 만들어줌
    sum = 0  
    c = 1   #같은 문자열 나오면 1씩 증가시키기
    for i in s :
        if i == 'O':
            sum+=c
            c += 1
        else :
            c = 1
    print(sum)





