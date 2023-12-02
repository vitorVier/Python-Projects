def main():

    print("Metodo de Ordenação")

    posições = int(input("\nInsira a quantidade de pessoas, empresas, entre outros: "))

    i = 0

    while i < posições:
        i = i + 1
        nome = input("{}: Insira o nome aqui: ".format(i).strip().capitalize())
        
main()