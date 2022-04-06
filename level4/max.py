#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

arr =[]
max =0
index =0
for i in range(1,9+1) :
    arr.append(int(input()))
for i in range(len(arr)) :
    if max < arr[i]  :
        max = arr[i]
        index = i +1 #인덱스가 0부터 시작하므로 문제는 1로 시작하니까 +1해주기

print(max,index)