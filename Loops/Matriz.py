linhas = int(input("Quantas linhas tem sua matriz?: "))
colunas = int(input("Quantas colunas tem sua matriz?: "))

Matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valores = int(input(f"Insira o valor contido em linha {i + 1}, coluna {j + 1}: "))
        linha.append(valores)
    Matriz.append(linha)

print("Matriz Inserida: ")

for linha in Matriz:
    print(linha)