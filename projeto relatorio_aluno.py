def media(nota1, nota2):
    media_calculada = (nota1 + nota2) / 2
    return media_calculada


def registrar_dados():
    disciplina = input("Digite o nome da disciplina: ")
    nome = input("Digite o nome do aluno: ")

    nota1, nota2, frequencia = 101, 101, 101

    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Digite a primeira nota (0 a 10): "))

    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Digite a segunda nota (0 a 10): "))

    while frequencia < 0 or frequencia > 100:
        frequencia = int(input("Digite a porcentagem de frequência (0 a 100): "))

    return nome, disciplina, nota1, nota2, frequencia


def calculo_frequencia(freq):
    return freq >= frequencia_minima


def geracao_relatorio(lista_final):
    print("\n=== RELATÓRIO FINAL DE TODAS AS TURMAS ===")

    for aluno in lista_final:
        print("Nome:", aluno["nome"])
        print("Disciplina:", aluno["disciplina"])
        print("Média:", aluno["media"])
        print("Frequência:", aluno["frequencia"])
        print("Situação:", aluno["situacao"])
        print("-" * 20)



alunos = []
nota_minima = 7.0
frequencia_minima = 75


for i in range(3):

    nome, disciplina, nota1, nota2, frequencia = registrar_dados()

    media_aluno = media(nota1, nota2)
    frequencia_ok = calculo_frequencia(frequencia)

    foi_aprovado = media_aluno >= nota_minima and frequencia_ok

    print("\nRESULTADO DO", nome.upper())
    print(f"Disciplina: {disciplina.upper()}")
    print("Média:", media_aluno)
    print("Frequência:", frequencia)

    if foi_aprovado:
        print("SITUAÇÃO: APROVADO")
    else:
        print("SITUAÇÃO: REPROVADO")

    if media_aluno < nota_minima:
        print("Motivo: Nota abaixo da média mínima.")

    if not frequencia_ok:
        print("Motivo: Frequência abaixo do permitido.")

    aluno = {
        "nome": nome,
        "disciplina": disciplina,
        "nota1": nota1,
        "nota2": nota2,
        "media": media_aluno,
        "frequencia": frequencia,
        "situacao": "APROVADO" if foi_aprovado else "REPROVADO"
    }

    alunos.append(aluno)

    if i < 2:  
        while True:
            opcao = input("\nDeseja encerrar o programa? (S/N): ")

            if opcao.upper() == "S":
                geracao_relatorio(alunos)
                exit()

            elif opcao.upper() == "N":
                break

            else:
                print("Opção inválida! Digite S ou N.")


geracao_relatorio(alunos)