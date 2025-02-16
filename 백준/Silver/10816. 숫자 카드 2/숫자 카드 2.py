n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dic = dict()
for i in n_list:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
        
ans = []
for i in m_list:
    if i in dic:
        ans.append(dic[i])
    else: ans.append(0)

for i in ans:
    print(i, end=' ')