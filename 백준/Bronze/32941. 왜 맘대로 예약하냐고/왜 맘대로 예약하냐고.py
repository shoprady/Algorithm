t, x = map(int, input().split())
for _ in range(int(input())):
    n = int(input())
    if x not in list(map(int, input().split())):
        print('NO'); exit(0)
print('YES')