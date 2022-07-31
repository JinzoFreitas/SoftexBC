# Softex - Recife
# Janderson Freitas
# Manipulando CSV com pandas

'''
Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:

aluno: Nome do aluno;
nota_1: Primeira nota;
nota_2: Segunda nota;
faltas: Número de faltas;

O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

Por fim, o programa deverá mostrar na tela:
- o maior número de faltas;
- a média geral das notas dos alunos;
- e a maior média.

'''

import pandas as pd
import csv

# Abre/Cria um arquivo .csv e escreve informnções nele. 
with open('1 - LP - POO/2- LP/Atividade 8/notas_alunos.csv', 'w', encoding='utf-8') as csvfile:
  csv.writer(csvfile, delimiter=',').writerow(['Amanda', '6', '3', '3'])
  csv.writer(csvfile, delimiter=',').writerow(['Bruno', '9', '7', '1'])
  csv.writer(csvfile, delimiter=',').writerow(['Caio', '3', '4', '2'])
  csv.writer(csvfile, delimiter=',').writerow(['David', '8', '6', '6'])
  csv.writer(csvfile, delimiter=',').writerow(['Ellen', '10', '9', '2'])
  csv.writer(csvfile, delimiter=',').writerow(['Felipe', '6', '8', '3'])
  csv.writer(csvfile, delimiter=',').writerow(['Gilbert', '8', '7', '7'])
  csv.writer(csvfile, delimiter=',').writerow(['Hilda', '9', '7', '1'])

# lendo o arquivo csv com pandas e criando o DataFrame. Arquivo sem cabeçalho.
df = pd.read_csv('1 - LP - POO/2- LP/Atividade 8/notas_alunos.csv', header = None)

# Definindo cabeçalho(Header) para a tabela de dados.
df.columns = ['Alunos','Nota_1','Nota_2','Faltas']

# Criando uma Coluna com a média das linhas de notas na transposta da tabela original(df.T). 
df['Média'] = df.T.loc['Nota_1':'Nota_2'].mean()

# Definindo uma condição com .loc para criar a coluna situação.
df.loc[((df['Média'] >= 7) & (df['Faltas'] <= 5)), ['Situação']] = 'Aprovado'
df.loc[((df['Média'] < 7) | (df['Faltas'] > 5)), ['Situação']] = 'Reprovado'

# Maior numero de falta
falta_max = df['Faltas'].max()

# Usando a função mean() para calcular a média total da turma.
media_turma = df['Média'].mean()

# Retorna o maior valor da coluna Média.
media_max = df['Média'].max()

# Criando Arquivo alunos_situação pois o metodo to_csv() requer um arquivo existente par gravar os dados.
with open('1 - LP - POO/2- LP/Atividade 8/alunos_situacao.csv', 'w', encoding='utf-8' ) as df_csv:
    # Salvando nosso DataFrame no arquivo que foi aberto para escrita. Sem uma coluna de index.
    df.to_csv(df_csv, index=False)

# Exibindo dataframe e os valores estatísticos da turma.
print(df)
print(f'\nO maior número de faltas por aluno foi: {falta_max}')
print(f'A média geral da turma foi: {media_turma}')
print(f'A maior média por aluno foi: {media_max}')