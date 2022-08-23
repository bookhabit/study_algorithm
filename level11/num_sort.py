num = []

n = int(input())
for i in range(n):
    s=int(input())
    num.append(s)
num.sort()
for i in range(len(num)):
    print(num[i])