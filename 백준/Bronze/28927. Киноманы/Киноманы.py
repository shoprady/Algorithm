a,b,c = map(int, input().split())
ma = 3*a+20*b+120*c
a,b,c = map(int, input().split())
me = 3*a+20*b+120*c
if ma > me: print('Max')
elif me > ma: print('Mel')
else: print('Draw')