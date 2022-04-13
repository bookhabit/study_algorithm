#입력
instr = input().upper()
many = []
a_instr = list(set(instr))

for i in a_instr:  #a_instr을 문자열 순서대로 many에 넣으니까 a_instr은 문자가 들어있고 many는 문자에 관한 count수가 들어가있음 서로 대응됨
    num = instr.count(i) #count가 반환하는 숫자의 개수
    many.append(num) 

if many.count(max(many)) >= 2 : #max(many)로 many리스트에서 가장 큰 값이 2개 이상이면 ?출력
    print("?")
else : #many리스트에서 가장 큰 값에 인덱스를 찾아서 a_instr에 인덱스로 값을 가져옴
    print(a_instr[many.index(max(many))])
    
