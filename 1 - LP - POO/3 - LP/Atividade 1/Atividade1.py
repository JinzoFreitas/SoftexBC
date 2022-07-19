# Softex - Recife
# Janderson Freitas
# Unidade 1 - Mód3 - Atividade 1

'''
Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve. Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:

- Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.

No sistema, todos os valores devem estar armazenados em variáveis.
'''
#Nesse Programa vamos utilizar listas para armazenar as informções do aluno, e vamos criar uma sala com 5 alunos.
'''
alunos, nota1, nota2, faltas = [""],[],[],[]

for i in range(4):
    alunos.append(input(f"Digite o nome do {(i+1)}º aluno: "))
    nota1.append(input(" Digite sua primeira nota: "))
    nota2.append(input(" Digite sua segunda nota: "))
    faltas.append(input(" Digite sua segunda nota: "))
'''


def dados():
    nome = input(f"Digite o nome do aluno: ")
    nota1 = float(input(" Digite sua primeira nota: "))
    nota2 = float(input(" Digite sua segunda nota: "))
    faltas = int(input(f" Digite quantas faltas {nome} tem: "))
    aprovacao(nome,nota1,nota2,faltas)

def aprovacao(nome, nota1, nota2, falta ):
    print(f"Aluno {nome}")
    media = (nota1 + nota2)/2
    if (media < 7):
        print(f"O Aluno {nome} está reprovado com média: {media}")
    elif (falta > 3):
        print(f"O Aluno {nome} está reprovado por falta, com {falta} faltas")
    else:
        print(f"O Aluno {nome} está Aprovado com média: {media}")    

if __name__ == "__main__":
    dados()
