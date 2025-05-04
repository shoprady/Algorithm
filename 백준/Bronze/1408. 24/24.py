t1, t2, t3 = map(int, input().split(':'))
s1, s2, s3 = map(int, input().split(':'))

k3 = s3 - t3
if k3 < 0:
    k3 += 60
    s2 -= 1

k2 = s2 - t2
if k2 < 0:
    k2 += 60
    s1 -= 1
    
k1 = s1 - t1
if k1 < 0:
    k1 += 24
    
print(f'{k1:02d}:{k2:02d}:{k3:02d}')