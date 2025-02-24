n = int(input())
people = list(map(int, input().split()))
people.sort()
ans = 0
for i in range(n):
    ans += people[i] * (n - i)
print(ans)