import sys
room = []
for _ in range(int(input())):
    i, j = map(int, sys.stdin.readline().split())
    room.append((i, j))
room.sort(key=lambda x: (x[1], x[0]))

ans, finish = 1, room[0][1]
for i in range(1, len(room)):
    if room[i][0] < finish: continue
    else: ans += 1; finish = room[i][1]
print(ans)