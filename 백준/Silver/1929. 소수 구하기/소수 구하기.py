import sys
input = sys.stdin.readline

m, n = map(int, input().split())
check = int(n ** 0.5)
for i in range(m, n + 1):
    if i == 1:
        continue
        
    flag = True
    for j in range(2, check + 1):
        if i % j == 0 and i != j:
            flag = False; break
    if flag:
        print(i)