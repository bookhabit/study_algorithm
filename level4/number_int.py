#세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
a=int(input())
b=int(input())
c=int(input())
#빈 배열
#계산한 결과를 배열에 넣고 배열에서 count()함수로 원소하나씩 구해보기
mul = a*b*c
mul = str(mul)
result = list(mul)  #list로 묶어주면 string을 하나씩 리스트에 원소로 넣어줌

#print(result.count('0'))  #count(x) x원소가 리스트에서 몇 개 있는지 반환

for i in range(10) : #1부터 9까지 반복
    print(result.count(str(i)))  #리스트 안에 문자열이니까 str로 변환
