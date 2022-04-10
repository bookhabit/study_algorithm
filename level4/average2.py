c = int(input())

for i in range(c):
    score =list(map(int,input().split( )))  #점수 리스트
    student = score.pop(0) #평균을 구함
    sum = 0
    for j in range(student):
        sum += score[j] 
    score_average = sum/student
    
    #평균을 넘는 학생들의 비율을 구하기 > 반올림하기 > 소수점 셋째자리까지 출력
    high_student = 0
    for i in score:
        if i > score_average :
            high_student +=1
    result = high_student/student*100 
    print(f'{result: .3f}%') #.3f 3째자리까지 실수
    
