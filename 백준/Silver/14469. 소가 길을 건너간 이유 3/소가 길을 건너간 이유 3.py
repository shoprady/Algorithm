n = int(input())
cows = []
for _ in range(n):
    cows.append(list(map(int, input().split())))
    
cows.sort()
time = 0
for i in range(len(cows)):
    time = max(time, cows[i][0])
    time += cows[i][1]
        
print(time)