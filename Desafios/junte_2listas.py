Vetor1 = int(input("Insira o número de alunos aqui?: "))

estudantes = []

for i in range(Vetor1):
    estudantes.append(input("Insira o nome do aluno {} aqui:".format(i + 1)))

for x in estudantes:
    print("Aluno {}: {}".format(estudantes.index(x),x))