g, s = [1,2,3,3,4,10], [1,2,2,2,3,5,10]
for i in range(1, int(input()) + 1):
    a, b = 0, 0
    ls1 = list(map(int, input().split()))
    ls2 = list(map(int, input().split()))
    for j in range(6):
        a += g[j] * ls1[j]
        b += s[j] * ls2[j]
    b += s[6] * ls2[6]
    if a < b: print(f'Battle {i}: Evil eradicates all trace of Good')
    elif a > b: print(f'Battle {i}: Good triumphs over Evil')
    else: print(f'Battle {i}: No victor on this battle field')