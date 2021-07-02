# while condição:
#   pass

# while True:  # looping infinito
#     nome = input("Qual o seu nome? ")
#     print(f'Olá {nome}!')
#
# print('não será executado')

# x = -2
# while x <= 15:
#     if x == 3:
#         x = x + 1
#         continue # não executa as linhas posteriores
#
#     print(x)
#     x = x + 1
# print('Acabou')

# while x <= 15:
#     if x == 3:
#         x = x + 1
#         break # sai do laço
#
#     print(x)
#     x = x + 1
# print('Acabou')

# x = 0  # coluna
# while x < 10:
#     y = 0  # linha
#     while y < 5:
#             print(f'({x},{y})')
#             y += 1
#     x += 1 # x = x + 1
# print('Acabou')

while True:
    num1 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    num2 = input('Digite um número: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número')
        sair = input("Desajar sair? [s]sim ou [n]ão? ")
        if sair == "s":
            break
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "*":
        print(num1 * num2)
    elif operador == "/":
        print('{:.2f}'.format(num1/num2))
    else:
        print("Operador inválido")

    sair = input("Desajar sair? [s]sim ou [n]ão? ")
    if sair == "s":
        break



