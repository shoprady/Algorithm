n = int(input())
cows = []
for _ in range(n):
    cows.append(list(map(int, input().split())))
    
cows.sort()
time = 0
for i in range(len(cows)):
    if time == 0:
        time += cows[i][0] + cows[i][1]
    elif time > cows[i][0]:
        time += cows[i][1]
    else:
        time = cows[i][0]
        time += cows[i][1]
        
print(time)