i, j = 2024, 8
j += (int(input()) - 1) * 7
while j > 12:
    i += 1; j -= 12
print(i, j)