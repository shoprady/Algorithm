t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0: print(0); continue
        
    dic = dict()
    for _ in range(n):
        clothes = input().split()
        if clothes[1] in dic:
            dic[clothes[1]].append(clothes[0])
        else: dic[clothes[1]] = [clothes[0]]
    
    if len(dic.keys()) == 1:
        print(len(dic[clothes[1]])); continue
        
    count = []
    for i in dic:
        count.append(len(dic[i]))
    ans = count[0] + 1
    for i in range(1, len(count)):
        ans *= count[i] + 1
    print(ans - 1)