n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

# t-shirt
shirts = 0
for size in sizes:
    if size == 0:
        continue
    elif size <= t:
        shirts += 1
    elif size % t == 0:
        shirts += size // t
    else:
        shirts += size // t + 1
print(shirts)

# pen
pens = n // p
pen = n % p
print(pens, pen)