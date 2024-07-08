a, b = map(int, input().split())

# a < b이도록 정렬
if b < a:
    temp = a
    a = b
    b = temp

# b가 a로 나누어떨어질 경우
if b % a == 0:
    x, y = a, b
    
else:
    # 최대공약수
    for i in range(1, a):
        if a % i == 0:
            if b % i == 0:
                x = i
    
    # 최소공배수
    order = 2
    while True:
        y = a * order
        if y % b == 0:
            break
        order += 1
    
print(x)
print(y)