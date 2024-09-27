n = int(input())
for order in range(n):
    stack = []
    str_list = input().split()
    for s in str_list:
        stack.append(s)
    print(f"Case #{order + 1}: ", end='')
    while stack:
        print(stack.pop(), end=' ')