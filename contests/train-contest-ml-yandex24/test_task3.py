jwellerys, stones = input(), input()

summa = 0
for stone in stones:
    if stone in jwellerys:
        summa += 1

print(summa)