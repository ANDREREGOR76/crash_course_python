number = input("Digite um número para saber se ele é impar ou par: ")
number = int(number)

if number % 2 == 0:
    print(f'O número {number} é par')
else:
    print(f'O número {number} é impar')
