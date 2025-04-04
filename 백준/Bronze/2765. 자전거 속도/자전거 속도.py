i = 1
while True:
    j, h, g = map(float, input().split())
    if h == 0.0: break
    dist = 3.1415927 * j * h / 63360
    time = g / 3600
    print('Trip #{0}: {1:.2f} {2:.2f}'.format(i, dist, dist / time))
    i += 1