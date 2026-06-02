# Programacao-de-computadores
Sistema de Controle de Notas e Frequência

Descrição

Este projeto foi desenvolvido em Python com o objetivo de realizar o cadastro de alunos, registrar notas e frequência, calcular médias e informar se o aluno foi aprovado ou reprovado de acordo com critérios pré-definidos.

O sistema permite cadastrar até 3 alunos, exibindo o resultado individual de cada um e, ao final, gerando um relatório completo com todos os registros.

Funcionalidades Cadastro do nome do aluno; Cadastro da disciplina; Registro de duas notas; Registro da frequência do aluno; Cálculo automático da média; Verificação da frequência mínima exigida; Exibição da situação do aluno (Aprovado ou Reprovado); Geração de relatório final com todos os alunos cadastrados; Opção de encerrar o programa antes do limite de cadastros. Regras de Aprovação

Para ser aprovado, o aluno deve:

Obter média igual ou superior a 7,0; Possuir frequência igual ou superior a 75%.

Caso não cumpra um desses requisitos, o aluno será considerado reprovado.

Estrutura do Código Função media(nota1, nota2)

Calcula a média aritmética das duas notas informadas.

Função registrar_dados()

Recebe os dados do aluno:

Nome; Disciplina; Primeira nota; Segunda nota; Frequência.

Também realiza validações para garantir que os valores estejam dentro dos limites permitidos.

Função calculo_frequencia(freq)

Verifica se a frequência do aluno atende ao mínimo exigido.

Função geracao_relatorio(lista_final)

Exibe um relatório contendo:

Nome do aluno; Disciplina; Média; Frequência; Situação final. Tecnologias Utilizadas Python 3 Exemplo de Saída

RESULTADO DO JOÃO

Disciplina: MATEMÁTICA

Média: 8.5

Frequência: 90

SITUAÇÃO: APROVADO

Objetivo Educacional

Este projeto foi desenvolvido para praticar conceitos fundamentais de programação em Python, incluindo:

Funções; Estruturas de repetição (while e for); Estruturas condicionais (if/else); Listas; Dicionários; Entrada e saída de dados; Validação de informações; Organização modular do código.
