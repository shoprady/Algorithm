for _ in range(int(input())):
    t = int(input()) % 25
    print("ONLINE") if t < 17 else print("OFFLINE")