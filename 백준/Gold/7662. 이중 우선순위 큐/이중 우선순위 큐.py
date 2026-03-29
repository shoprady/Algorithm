import heapq
for _ in range(int(input())):
    min_q, max_q = [], []
    k = int(input())
    deleted = [False] * k
    
    for i in range(k):
        cmd, val = input().split()
        if cmd == 'I':
            val = int(val)
            heapq.heappush(min_q, (val, i))
            heapq.heappush(max_q, (-val, i))
        else:
            if val == '-1':
                while min_q and deleted[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    n, k = heapq.heappop(min_q)
                    deleted[k] = True
            else:
                while max_q and deleted[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    n, k = heapq.heappop(max_q)
                    deleted[k] = True

    while min_q and deleted[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and deleted[max_q[0][1]]:
        heapq.heappop(max_q)

    if not min_q:
        print('EMPTY')
    else:
        print(-max_q[0][0], min_q[0][0])