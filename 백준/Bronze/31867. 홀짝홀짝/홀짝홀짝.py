n = int(input())
num = input()
odd, even = 0, 0
for i in num:
    if int(i) % 2 == 1: odd += 1
    else: even += 1
if odd < even: print(0)
elif odd > even: print(1)
else: print(-1)