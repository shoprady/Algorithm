n, p = int(input()), int(input())
discount = [0]
if n >= 5: discount.append(500)
if n >= 10: discount.append(p * 10 // 100)
if n >= 15: discount.append(2000)
if n >= 20: discount.append(p * 25 // 100)
print(max(0, p - max(discount)))