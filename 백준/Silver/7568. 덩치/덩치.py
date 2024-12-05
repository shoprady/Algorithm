n = int(input())
ans, people = [1 for _ in range(n)], []
for _ in range(n):
    people.append(list(map(int, input().split())))

for i in range(n):
    curr = 0
    while curr < n:
        if people[i][0] < people[curr][0] and people[i][1] < people[curr][1]:
            ans[i] += 1
        curr += 1
            
for i in ans:
    print(i, end=' ')