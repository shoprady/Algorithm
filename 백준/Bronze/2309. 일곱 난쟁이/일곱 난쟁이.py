heights = []
for _ in range(9):
    heights.append(int(input()))

check = False
for i in range(9):
    for j in range(i + 1, 9):        
        if sum(heights) - heights[i] - heights[j] == 100:
            a, b = heights[i], heights[j]
            check = True
    if check == True:
        break

heights.remove(a)
heights.remove(b)

for h in sorted(heights):
    print(h)