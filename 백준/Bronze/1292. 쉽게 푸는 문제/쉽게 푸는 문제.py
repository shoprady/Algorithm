a, b = map(int, input().split())
start, end, num, sum = 1, 1, 1, 0

while a not in range(start, end + 1):
    num += 1
    end += num
    start = end - num + 1

for i in range(a, b + 1):
    if i in range(start, end + 1):
        sum += num
    else:
        num += 1
        end += num
        start = end - num + 1
        sum += num

print(sum)