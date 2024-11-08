def get_left(list, value):
    first = 0
    last = len(list) - 1
    while first < last:
        mid = (first + last) // 2
        if list[mid] >= value:
            last = mid
        else:
            first = mid + 1
    if list[first] >= value:
        return len(list) - first
    else: return 0
    
def get_right(list, value):
    first = 0
    last = len(list) - 1
    while first < last:
        mid = (first + last) // 2
        if list[mid] <= value:
            first = mid + 1
        else:
            last = mid
    if list[last] > value:
        return len(list) - last
    else: return 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        k = query[1]
        print(get_left(arr, k))
        
    elif query[0] == 2:
        k = query[1]
        print(get_right(arr, k))
            
    else: # query[0] == 3
        i, j = query[1], query[2]
        print(get_left(arr, i) - get_right(arr, j))