#이 문제는 랜덤으로 숫자 N이 주어질 때 1이 있는 벌집 위치에서 숫자 N까지 거쳐가는 단계의 수를 찾아내는 문제이다. 다시 말해서 숫자 N이 벌집에서 몇 겹째에 있는지를 출력하는 문제이다.
n = int(input())

cnt= 1 
nums = 1 # 벌집의 개수 , 1개부터 시작
while n > nums :  # nums는 1부터 시작하고 6의 배수로 6의배수일때만 1더해줌
    nums = nums + (cnt *6)
    #print(nums)
    cnt += 1
print(cnt)        
    
