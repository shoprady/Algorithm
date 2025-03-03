n = int(input())
ls = [int(i) % 2 for i in input().split()]
print('Happy' if ls.count(0) > ls.count(1) else 'Sad')