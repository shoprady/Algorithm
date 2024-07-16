N = int(input())
heights = []

for _ in range(N):
    heights.append(int(input()))

sum = 0
stack = []
for h in heights:
    while stack and stack[-1] <= h:
        stack.pop()
    stack.append(h)
    
    if len(stack) > 1:
        sum += len(stack) - 1
            
print(sum)