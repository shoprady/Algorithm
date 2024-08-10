T = int(input())
for _ in range(T):
    string = list(input())
    score, temp = 0, 0
    for s in string:
        if s == "O":
            score += temp + 1
            temp += 1
        else:
            temp = 0
    print(score)