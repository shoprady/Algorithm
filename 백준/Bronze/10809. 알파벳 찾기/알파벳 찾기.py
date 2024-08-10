string = list(input())
alphabets = [-1 for _ in range(26)]

for s in string:
    alpha = ord(s) - 97
    alphabets[alpha] = string.index(s)
    
for a in alphabets:
    print(a, end=" ")