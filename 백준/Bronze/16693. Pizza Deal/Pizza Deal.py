from math import pi

a1, p1 = map(int, input().split())
slice_price = a1 / p1

r1, p2 = map(int, input().split())
a2 = r1 ** 2 * pi
whole_price = a2 / p2

if slice_price > whole_price:
    print("Slice of pizza")
else:
    print("Whole pizza")