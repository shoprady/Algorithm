pic = [input().split() for _ in range(15)]
for i in range(15):
    for j in range(15):
        if pic[i][j] == 'w': print('chunbae'); exit(0)
        elif pic[i][j] == 'b': print('nabi'); exit(0)
        elif pic[i][j] == 'g': print('yeongcheol'); exit(0)