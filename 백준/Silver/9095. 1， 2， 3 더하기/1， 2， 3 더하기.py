t = int(input())
ans = []
for _ in range(t):
    ans.append(int(input()))
arr = [0] * 11;
arr[0], arr[1], arr[2] = 1, 2, 4
for i in range(3, 11):
    arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1]
for i in ans:
    print(arr[i - 1])