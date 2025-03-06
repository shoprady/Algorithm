n = int(input())
pages = list(map(int, input().split()))
for i in range(len(pages)):
    if pages[i] % 2 == 1:
        pages[i] += 1
print(sum(pages) // 2)