n = int(input())

# 규칙 long이 하나당 4바이트 추가
# 만약 20바이트라면 long이 5개
long_type_number =  int(n/4)
for i in range(long_type_number):
    print('long',end=" ")

print('int')