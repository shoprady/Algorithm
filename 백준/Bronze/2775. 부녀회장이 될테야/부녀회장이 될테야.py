t = int(input())
floors, rooms = [], []
for _ in range(t):
    floors.append(int(input()))
    rooms.append(int(input()))

max_floor, max_room = max(floors) + 1, max(rooms)
apt = [[0 for _ in range(max_room)] for _ in range(max_floor)]

for i in range(max_floor):
    if i == 0:
        apt[0] = [i + 1 for i in range(max_room)]
        continue

    for j in range(max_room):
        curr = j
        while curr >= 0:
            apt[i][j] += apt[i - 1][curr]
            curr -= 1

for i in range(t):
    print(apt[floors[i]][rooms[i] - 1])