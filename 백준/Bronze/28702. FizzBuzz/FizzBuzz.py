for i in range(3):
    num = input()
    if num.isdigit():
        ans = int(num) - i + 3
        break
        
if ans % 3 == 0 and ans % 5 == 0:
    print("FizzBuzz")
elif ans % 3 == 0:
    print("Fizz")
elif ans % 5 == 0:
    print("Buzz")
else: print(ans)