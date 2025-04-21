for _ in range(int(input())):
    p1, p2 = 0, 0
    for _ in range(int(input())):
        ls = input().split()
        if ls[0] == ls[1]: continue
        elif (ls[0] == 'R' and ls[1] == 'S') or (ls[0] == 'S' and ls[1] == 'P') or (ls[0] == 'P' and ls[1] == 'R'):
            p1 += 1
        else: p2 += 1
    if p1 > p2: print('Player 1')
    elif p1 == p2: print('TIE')
    else: print('Player 2')