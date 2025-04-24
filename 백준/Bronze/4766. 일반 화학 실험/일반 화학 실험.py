tmp = -11
while True:
    n = input()
    if n == '999': break
    if tmp != -11:
        print('{:.2f}'.format(float(n) - tmp))
    tmp = float(n)