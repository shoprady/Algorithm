for case in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    score = 0
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            score += 1
    print(f"Case #{case+1}:", end=' ')
    print(0) if score == k else print(abs(score-k))