x = float(input('Enter the value of seed x: '))
a = float(input('Enter the value of a: '))
c = float(input('Enter the value of c: '))
m = float(input('Enter the value of m: '))
total = int(input('Enter the value of total Randoms: '))

randomNumbers = []

for i in range(total):
    x = (a * x + c) % m
    randomNumber = round(x / m, 3)
    if randomNumber in randomNumbers:
        print('Duplicate Random Number: ', randomNumber)
        break
    randomNumbers.append(randomNumber)

print(f'The random numbers are: {randomNumbers}')

