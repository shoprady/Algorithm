ans = []
for a in range(6, 101):
    for b in range(2, a):
        for c in range(b + 1, a):
            for d in range(c + 1, a):
                if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                    ans.append((a, b, c, d))
for a, b, c, d in ans:
    print(f'Cube = {a}, Triple = ({b},{c},{d})')