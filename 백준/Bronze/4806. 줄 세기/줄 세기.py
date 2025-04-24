n = 0
while True:
    try:
        s = input()
        n += 1
    except EOFError:
        break
print(n)