ans, s = [], input()
i = 0
while i < len(s):
    if s[i] in ['a','e','i','o','u']:
        i += 2
    ans.append(s[i])
    i += 1
print(''.join(ans))