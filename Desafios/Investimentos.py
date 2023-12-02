def main():
    
    print("Calculadora de Investimentos")

    inicial = float(input("\nQuantos reais voce deseja investir por mês?: "))
    tempo = float(input("Qual será o periodo de investimento em meses?: "))
    porcentagem = float(input("Qual a porcentagem de lucro por ano?: "))

    ano = tempo/12
    porcentagem_mes = porcentagem/12
    Investido = inicial * tempo
    LucroA = (inicial * porcentagem)
    LucroM = (LucroA / 12)
    Lucro_Final = (Investido + (Investido * porcentagem_mes)) - Investido

    print("\nValor investido por mês: R${:,}".format(inicial))
    print("Periodo de investimento em meses: {} meses".format(tempo))
    print("Periodo de investimento em anos: {} anos".format(ano))

    print("\nTotal Investido: R${:,}".format(Investido))
    print("Margem de lucro ao mês: R${:.2f} ao mes!".format(LucroM))
    print("Margem de lucro ao Ano: R${:.2f} ao ano!".format(LucroA))
    print("Lucro Final: R${:,}".format(Lucro_Final))

main()