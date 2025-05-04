alpha = [0] * 26
while True:
    try:
        s = input()
        for i in s:
            if i.isalpha():
                alpha[ord(i)-97] += 1
    except EOFError:
        break
m = max(alpha)
for i in range(26):
    if alpha[i] == m:
        print(chr(i+97), end='')