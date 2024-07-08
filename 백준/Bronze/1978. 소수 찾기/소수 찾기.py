N = int(input())
arr = list(map(int, input().split()))

for num in arr:
    if num == 1:
        N -= 1
        continue
        
    for i in range(2, num):
        if num % i == 0:
            N -= 1
            break
            
print(N)