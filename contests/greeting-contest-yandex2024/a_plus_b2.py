with open('input.txt', 'r') as file:
    num1, num2 = map(int, file.readline().split())
    summa = num1 + num2
    with open('output.txt', 'w') as file:
        file.write(str(summa))