# Softex - Recife
# Janderson Freitas
# Unidade 1 - Mód3 - Atividade 1

'''
Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve.
Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:
- Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.
No sistema, todos os valores devem estar armazenados em variáveis.
'''

def main():
    nome = input(f"Digite o nome do aluno: ")
    nota1 = float(input(" Digite sua primeira nota: "))
    nota2 = float(input(" Digite sua segunda nota: "))
    faltas = int(input(f" Digite quantas faltas {nome} tem: "))
    aprovacao(nome,nota1,nota2,faltas)

def aprovacao(nome, nota1, nota2, falta ):

    media = (nota1 + nota2)/2
    if (media < 7):
        print(f"\nO Aluno {nome} está reprovado com média: {media}")
    elif (falta > 3):
        print(f"\nO Aluno {nome} está reprovado com {falta} faltas")
    else:
        print(f"\nO Aluno {nome} está Aprovado com média {media}")    

main()
