i = int(input('Pls enter the profit:'))
base = [1000000, 600000, 400000, 200000, 100000, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
for a in range(0,6):
    if i > base[a]:
        bonus += (i - base[a]) * rate[a]
print(bonus)
