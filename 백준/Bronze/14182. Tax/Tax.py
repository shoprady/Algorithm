while True:
    n = int(input())
    if n == 0: break
    if n <= 1000000: print(n)
    elif n <= 5000000: print(n*90//100)
    else: print(n*80//100)