while True:
    info = input().split()
    if info[0] == '#': break
    if int(info[1]) > 17 or int(info[2]) >= 80:
        print(info[0], 'Senior')
    else: print(info[0], 'Junior')