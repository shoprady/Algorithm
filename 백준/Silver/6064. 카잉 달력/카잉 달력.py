import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    ans, count = 0, x
    max_count = math.lcm(m, n)
    while count <= max_count:
        if (count - x) % m == 0 and (count - y) % n == 0:
            ans = count; break
        count += m
    print(ans) if ans else print(-1)