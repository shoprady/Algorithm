i = 0
n = int(input())
for _ in range(n):
    if int(input()): i += 1
print("Junhee is cute!") if i>n//2 else print("Junhee is not cute!")