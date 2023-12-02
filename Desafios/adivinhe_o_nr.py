import random

def main():
    numero_secreto = random.randint(1,500)
    tentativas_max = 10
    tentativas = 0

    print("Bem Vindo!")
    print("Tente adivinhar o número secreto! O número está entre 1 e 500")
    print(f"Voce tem {tentativas_max} tentativas")

    while tentativas < tentativas_max:
        palpite = int(input("\nTentativa {}: Digite um número: ".format(tentativas + 1)))

        if palpite == numero_secreto:
            print("Parabéns! Voce acertou em {} tentativas".format(tentativas + 1))
            break

        elif palpite < numero_secreto:
            print("Voce errou! Tente um valor mais alto!")

        else:
            print("Voce errou! Tente um valor mais baixo!")

        tentativas += 1

        if tentativas == tentativas_max:
            print("Suas chances acabaram. O número secreto era {}".format(numero_secreto))

main()