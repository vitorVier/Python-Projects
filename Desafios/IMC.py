print("Calculadora de IMC")

def main():
    peso = float(input("Insira aqui o seu peso(kg): "))
    altura = float(input("Insira aqui sua altura(m): "))
    IMC = peso/(altura*altura)
    print("\nPeso: {}".format(peso))
    print("Altura: {}".format(altura))
    print("\nIMC: {}\n".format(IMC))

    if IMC < 18.5:
        print("Classificação: Abaixo do peso")

    elif IMC >= 18.5 and IMC <= 24.9:
        print("Classificação: Peso Normal") 

    elif IMC <= 25 and IMC <= 29.9:
        print("Classificação: Sobrepeso") 

    elif IMC <= 30 and IMC <= 34.9:
        print("Classificação: Obesidade Grau 1")

    elif IMC <= 35 and IMC <= 39.9:
        print("Classificação: Obesidade Grau 2")
    
    elif IMC > 40:
        print("Classificação: Obesidade Grau 3")

    else: 
        print("ERROR")

main()