def fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1 ):
        fatorial *= i
    return fatorial

print("Calculadora Fatorial")

def main():

    numero = int(input("Digite um valor inteiro: "))

    resultado = fatorial(numero)
    print("O fatorial de {} é {}.".format(numero, resultado))

main()