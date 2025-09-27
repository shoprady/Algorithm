while True:
    a,b,c,d = map(int, input().split())
    if a==b==c==d==0: break
    elif a==b==c==d: print(0); continue
    ls, ans, nxt = [a,b,c,d], 0, []
    while True:
        ans += 1
        nxt = [abs(ls[0]-ls[1]), abs(ls[1]-ls[2]), abs(ls[2]-ls[3]), abs(ls[3]-ls[0])]
        if nxt[0]==nxt[1]==nxt[2]==nxt[3]: break
        ls = nxt
    print(ans)