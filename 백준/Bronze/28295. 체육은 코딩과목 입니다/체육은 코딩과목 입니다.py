d, dic = 0, {0:'N', 1:'E', 2:'S', 3:'W'}
for _ in range(10):
    d += int(input())
print(dic[d % 4])