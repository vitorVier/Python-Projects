def main():
    print("Calculadora de Desconto")
    print("\nInsira o valor em Reais e a porcentagem em decimais: ex: 10% = 0.10")

    valor_original = int(input("\nInsira o valor original do produto: "))
    desconto = float(input("\nInsira a porcentagem do desconto: "))
    resultado = valor_original - (valor_original*desconto) 
    porcentagem = desconto*100
    economia = valor_original - resultado

    if desconto < 0 or desconto > 100:
        print("Valor do desconto invalido!")

    else:
        print("\nValor original: R${:,}".format(valor_original))
        print("Desconto: {}%".format(porcentagem))
        print("Valor Final com desconto aplicado: R${:,} reais!".format(resultado))
        print("Valor Economizado: R${:,}".format(economia))

main()