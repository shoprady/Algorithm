import sys
sys.setrecursionlimit(int(2e4))

def postorder(left, right):
    if left > right:
        return
    mid = right + 1
    for i in range(left + 1, right + 1):
        if pre[i] > pre[left]:
            mid = i; break
    postorder(left + 1, mid - 1)
    postorder(mid, right)
    print(pre[left])

pre = []
while True:
    try:
        pre.append(int(input()))
    except: break
        
postorder(0, len(pre) - 1)