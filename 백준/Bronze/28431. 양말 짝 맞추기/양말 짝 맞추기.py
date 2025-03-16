socks = []
for _ in range(5):
    i = int(input())
    if i in socks: socks.remove(i)
    else: socks.append(i)
print(socks[0])