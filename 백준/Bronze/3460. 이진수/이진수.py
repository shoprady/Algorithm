T = int(input())
for _ in range(T):
    n = int(input())
    bit = "".join(reversed(bin(n)[2:]))
    order = 0
    for _ in bit:
        if bit[order] == '1':
            print(order, end=" ")
        order += 1