n = int(input())
d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in input():
    d[i] += 1
print(d['A'] * d['C'] * d['G'] * d['T'] % 1000000007)