maior_notaA, maior_notaB, maior_notaC, maior_notaD, maior_nota1 = 0,0,0,0,0
alunoA, alunoB, alunoC, alunoD, aluno1 = "","","","",""
countA, countB, countC, countD, count = 0,0,0,0,0

print("Alunos da turma A") 
for x in range(0,3):
  nome = input("Digiti seu nome:")
  nota = float(input("Digite sua nota do vestibular: "))
  if nota >= 7 :
    countA = countA + 1
  if nota > maior_notaA :
    maior_notaA = nota
    alunoA = nome
  elif nota == maior_notaA :
    alunoA = alunoA + "; " + nome

if maior_notaA > maior_nota1 :
  maior_nota1 = maior_notaA
  aluno1 = alunoA
elif maior_notaA == maior_nota1 :
  aluno1 = aluno1 + ", " + alunoA

print("Alunos da turma B")
for x in range(0,3):
  nome = input("Digiti seu nome:")
  nota = float(input("Digite sua nota do vestibular: "))
  if nota >= 7 :
    countB = countB + 1
  if nota > maior_notaB :
    maior_notaB = nota
    alunoB = nome
  elif nota == maior_notaB :
    alunoB = alunoB + "; " + nome

if maior_notaB > maior_nota1 :
  maior_nota1 = maior_notaB
  aluno1 = alunoB
elif maior_notaB == maior_nota1 :
  aluno1 = aluno1 + "; " + alunoB

print("Alunos da turma C")
for x in range(0,3):
  nome = input("Digiti seu nome:")
  nota = float(input("Digite sua nota do vestibular: "))
  if nota >= 7 :
    countC = countC + 1
  if nota > maior_notaC :
    maior_notaC = nota
    alunoC = nome
  elif nota == maior_notaC :
    alunoC = alunoC + "; " + nome   

if maior_notaC > maior_nota1 :
  maior_nota1 = maior_notaC
  aluno1 = alunoC
elif maior_notaC == maior_nota1 :
  aluno1 = aluno1 + "; " + alunoC   

print("Alunos da turma D")
for x in range(0,3):
  nome = input("Digiti seu nome:")
  nota = float(input("Digite sua nota do vestibular: "))
  if nota >= 7 :
    countD = countD + 1
  if nota > maior_notaD :
    maior_notaD = nota
    alunoD = nome
  elif nota == maior_notaD :
    alunoD = alunoD + "; " + nome 

if maior_notaD > maior_nota1 :
  maior_nota1 = maior_notaD
  aluno1 = alunoD
elif maior_notaD == maior_nota1 :
  aluno1 = aluno1 + "; " + alunoD

count = countA + countB + countC + countD

print(f"{count} Alunos passaram no vestibular esse ano!")
print("")
print(f"{countA} da Turma A")
print(f"{countB} da Turma B")
print(f"{countC} da Turma C")
print(f"{countD} da Turma D")
print("")
print(f"o Aluno {alunoA}, foi o primeiro lugar da Turma A com nota {maior_notaA}") 
print(f"o Aluno {alunoB}, foi o primeiro lugar da Turma B com nota {maior_notaB}") 
print(f"o Aluno {alunoC}, foi o primeiro lugar da Turma C com nota {maior_notaC}") 
print(f"o Aluno {alunoD}, foi o primeiro lugar da Turma D com nota {maior_notaD}")
print("")
print(f"o Aluno {aluno1}, foi o primeiro lugar geral com nota {maior_nota1}")