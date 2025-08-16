for _ in range(int(input())):
    cm, kg = map(int, input().split())
    bmi = kg / (cm/100)**2
    if cm < 140.1:
        print(6)
    elif cm < 146:
        print(5)
    elif cm < 159 or cm >= 204:
        print(4)
    elif bmi < 16.0 or bmi >= 35.0:
        print(4)
    elif 16.0 <= bmi < 35.0 and 159 <= cm < 161:
        print(3)
    elif 161 <= cm < 204:
        if (16.0 <= bmi < 18.5) or (30.0 <= bmi < 35.0):
            print(3)
        elif (18.5 <= bmi < 20.0) or (25.0 <= bmi < 30.0):
            print(2)
        else: print(1)