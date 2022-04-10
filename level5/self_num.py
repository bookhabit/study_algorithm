def d(n): #셀프넘버를 아닌 것을 리턴하는 함수 (생성자가 있는 숫자)
    for i in str(n):
        n += int(i)
    return n

numbers = set(range(1, 10000))
remove_set = set()  # 생성자가 있는 숫자 set

for num in numbers :
    remove_set.add(d(num))  # add: 집합에 요소를 추가할 때

self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
for self_num in sorted(self_numbers):  # sorted 함수로 정렬
    print(self_num)

#     #생성자가 존재하지 않는 숫자 > 셀프넘버