i = 1
while True:
    s = input()
    if s == '0': break
    r, w, l = map(int, s.split())
    d = (w**2 + l**2) ** 0.5
    if d <= 2*r: print(f"Pizza {i} fits on the table.")
    else: print(f"Pizza {i} does not fit on the table.")
    i += 1