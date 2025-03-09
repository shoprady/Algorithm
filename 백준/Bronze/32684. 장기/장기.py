cho = list(map(int, input().split()))
han = list(map(int, input().split()))
score = [13, 7, 5, 3, 3, 2]

for i in range(6):
    cho[i] *= score[i]
    han[i] *= score[i]
    
print('cocjr0208') if sum(cho) > sum(han) + 1.5 else print('ekwoo')