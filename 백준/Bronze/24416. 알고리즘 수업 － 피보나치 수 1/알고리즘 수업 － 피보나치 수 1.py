ans = 0
def fib(n):
    global ans
    if n == 1 or n == 2:
        ans += 1; return 1
    else: return fib(n - 1) + fib(n - 2)

n = int(input())
fib(n)
print(ans, n - 2)