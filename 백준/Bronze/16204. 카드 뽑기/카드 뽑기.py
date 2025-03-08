n, m, k = map(int, input().split())
f_o, f_x = m, n - m
b_o, b_x = k, n - k
print(min(f_o, b_o) + min(f_x, b_x))