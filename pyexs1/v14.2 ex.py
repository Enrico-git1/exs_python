n1 = input("Digite um número inteiro: ")
try:
    n1 = int(n1)

    if n1 % 2 == 0:
        print("Par")
    else:
        print('Ímpar')
except:
    print("Não é um número inteiro")
