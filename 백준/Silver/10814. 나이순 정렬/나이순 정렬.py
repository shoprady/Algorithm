import sys
input = sys.stdin.readline

n = int(input())
people = []
for i in range(n):
    people.append(input().split())
    people[i][0] = int(people[i][0])
people.sort(key=lambda x: x[0])
for a, b in people:
    print(a, b)