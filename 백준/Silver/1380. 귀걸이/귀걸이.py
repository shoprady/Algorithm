t = 1
while True:
    n = int(input())
    if n == 0: break
    name = []
    for _ in range(n):
        name.append(input())
    ear = dict()
    for _ in range(2*n-1):
        num, order = input().split()
        num = int(num)
        if num in ear: ear[num] += 1
        else: ear[num] = 1
    for i in ear:
        if ear[i] == 1:
            print(f'{t} {name[i-1]}')
            break
    t += 1