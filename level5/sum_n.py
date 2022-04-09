#정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
def solve(a):  # a매개변수는 list형태이고  int값을 반환함
    sum=0
    for i in a:
        sum += i
    return sum
