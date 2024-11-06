n = int(input())
ls = list(map(int, input().split()))
dic = {num: True for num in ls}

m = int(input())
ans = list(map(int, input().split()))

for num in ans:
    if num in dic:
        print(1)
    else: print(0)