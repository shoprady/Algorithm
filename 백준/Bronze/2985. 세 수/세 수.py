a, b, c = map(int, input().split())
if a + b == c:
    print('{0}+{1}={2}'.format(a, b, c))
elif a - b == c:
    print('{0}-{1}={2}'.format(a, b, c))
elif a * b == c:
    print('{0}*{1}={2}'.format(a, b, c))
elif a // b == c:
    print('{0}/{1}={2}'.format(a, b, c))
elif a == b + c:
    print('{0}={1}+{2}'.format(a, b, c))
elif a == b - c:
    print('{0}={1}-{2}'.format(a, b, c))
elif a == b * c:
    print('{0}={1}*{2}'.format(a, b, c))
else:
    print('{0}={1}/{2}'.format(a, b, c))