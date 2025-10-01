ls = []
for _ in range(3):
    ls.append(list(map(int, input().split())))
if ls[1][0]-ls[0][0]:
    a = (ls[1][1]-ls[0][1])/(ls[1][0]-ls[0][0])
    b = ls[1][1] - ls[1][0]*a
    print("WHERE IS MY CHICKEN?") if ls[2][1] == a*ls[2][0] + b else print("WINNER WINNER CHICKEN DINNER!")
else:
    print("WHERE IS MY CHICKEN?") if ls[2][0] == ls[0][0] else print("WINNER WINNER CHICKEN DINNER!")