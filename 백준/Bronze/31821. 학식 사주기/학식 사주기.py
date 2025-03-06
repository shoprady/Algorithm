menu = []
for _ in range(int(input())):
    menu.append(int(input()))
total = 0
for _ in range(int(input())):
    total += menu[int(input()) - 1]
print(total)