#시험 성적
score = input()
score = int(score)

#print(A,B)
if 90 <= score <= 100 :
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79 :
    print('C')
elif 60 <= score <= 69 :
    print('D')
else :
    print('F')
    