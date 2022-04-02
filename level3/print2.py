# 조건이 없다면 반복문은 무한루프가 도므로 더이상 입력이없다면
#try except구문으로 break로 반복문을 끝낸다
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break