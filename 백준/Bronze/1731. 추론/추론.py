ls = []
for _ in range(int(input())):
    ls.append(int(input()))
check = (ls[2]-ls[1] == ls[1]-ls[0])
print(ls[-1]+ls[1]-ls[0]) if check else print(ls[-1]*ls[1]//ls[0])