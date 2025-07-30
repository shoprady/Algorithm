a, x = int(input()), int(input())
if a >= x:
    print('Congratulations, you are within the speed limit!')
elif a + 20 >= x:
    print('You are speeding and your fine is $100.')
elif a + 30 >= x:
    print('You are speeding and your fine is $270.')
else:
    print('You are speeding and your fine is $500.')