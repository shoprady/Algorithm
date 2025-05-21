s = input()
a, b = 0, 0
for i in s:
    if i == ':': a += 1
    elif i == '_': b += 1
print(len(s) + a + b * 5)