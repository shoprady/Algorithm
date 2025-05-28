l, t = 0, 0
try:
    while True:
        if input() == 'Lion': l += 1
        else: t += 1
except:
    print('Lion') if l > t else print('Tiger')