# 알파벳 소문자로만 이루어진 단어 s 가 주어진다
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오
from string import ascii_lowercase
s = input()

 
alpha_list = list(ascii_lowercase) #알파벳배열
for i in range(len(alpha_list)):
    if alpha_list[i] in s :  #배열의 원소가 s문자열에 있다면
        print(s.index(alpha_list[i]))
    else:
        print(-1)
    
