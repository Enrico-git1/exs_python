n1 = input("Qual a hora? ")

if n1.isnumeric():
    n1 = int(n1)
    if n1 >= 0 and n1 <= 11:
        print('Bom dia!')
    elif n1 >= 12 and n1 <= 17:
        print('Boa tarde!')
    elif n1 >= 18 and n1 <= 23:
        print('Boa noite!')
else:
    print('Digite um valor apropriado')