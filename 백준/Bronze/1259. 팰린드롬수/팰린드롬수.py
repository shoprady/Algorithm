while True:
    num = input()
    if num == '0': break
    if num == ''.join(reversed(num)): print("yes")
    else: print("no")