def verificar_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True  


def main():
    
    numero = int(input("Insira um número inteiro positivo: "))

    if verificar_primo(numero):
            print("{} é um número primo!".format(numero))

    else:
            print("{} não é primo!".format(numero))

main()