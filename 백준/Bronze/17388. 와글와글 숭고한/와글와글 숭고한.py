s, k, h = map(int, input().split())
dic = {s: 'Soongsil', k: 'Korea', h: 'Hanyang'}
if s+k+h >= 100: print('OK')
else: print(dic[min(s, k, h)])