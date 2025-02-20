import math

n = int(input())
if n == 0:
    print(0)
    exit(0)
    
levels = []
for _ in range(n):
    levels.append(int(input()))

# sorting algorithm
levels.sort()

total = len(levels)
delete = math.floor(total / 100 * 15 + 0.5)

levels = levels[:total - delete]
levels = levels[delete:]
print(math.floor(sum(levels) / len(levels) + 0.5))