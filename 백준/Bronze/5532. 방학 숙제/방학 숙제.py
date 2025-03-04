l, a, b, c, d =  int(input()), int(input()), int(input()), int(input()), int(input())
hw1, hw2 = 0, 0
hw1 += a // c; a -= hw1 * c
if a > 0: hw1 += 1
hw2 += b // d; b -= hw2 * d
if b > 0: hw2 += 1
print(l - max(hw1, hw2))