import sys
nums_dict = {}
for i in range(1, 10001):
    nums_dict[i] = 0
    
n = int(sys.stdin.readline())
for _ in range(n):
    nums_dict[int(sys.stdin.readline())] += 1
    
for i in nums_dict:
    for _ in range(nums_dict[i]):
        print(i)