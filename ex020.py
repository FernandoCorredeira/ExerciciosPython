num = list(range(10))

for n in num:
    num[n] = int(input('Digite um número: '))

for n in range(0, 10):
    if n % 2 != 0:
        print(num[n])