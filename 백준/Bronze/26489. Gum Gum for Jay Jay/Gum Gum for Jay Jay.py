ans = 0
while True:
    try:
        if input(): ans += 1
    except:
        break
print(ans)