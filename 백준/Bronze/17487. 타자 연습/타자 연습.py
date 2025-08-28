ls = ['q', 'w', 'e', 'r', 't', 'y', \
      'a', 's', 'd', 'f', 'g', \
      'z', 'x', 'c', 'v', 'b']
s = input()
left = right = other = 0
for i in s:
    if i.isupper(): other += 1
    if i.lower() in ls:
        left += 1
    elif i == ' ':
        other += 1
    else:
        right += 1
while other > 0:
    if left > right:
        right += 1
    else:
        left += 1
    other -= 1
print(left, right)