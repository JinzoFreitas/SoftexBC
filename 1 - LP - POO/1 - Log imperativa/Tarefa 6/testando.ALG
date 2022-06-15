Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 15/06/2022
Var


nome, aluno_primeiro : Caracter
x, aprovadosA, aprovadosB, aprovadosC, aprovadosD : Inteiro
nota, notamaxA, notamaxB, notamaxC, notamaxD : Real


Inicio


escreval("Alunos Truma A")
para x de 1 ate 2 faca
  escreva("Digite o nome do aluno:")
  leia(nome)
  escreva("Digite a nota do aluno:")
  leia(nota)
  se (nota >= 7) entao
    aprovadosA <- aprovadosA + 1
  se (nota > notamaxA) entao
    notamaxA <- nota
    aluno_primeiro <- nome
  senao
    se (nota == notamaxA) entao
      aluno_primeiro <- aluno_primeiro + ", " + nome
    fimse
  fimse
fimpara

escreva("Alunos Truma B")
para x de 1 ate 2 faca
  escreva("Digite o nome do aluno:")
  leia(nome)
  escreva("Digite a nota do aluno:")
  leia(nota)
  se (nota > 7) entao
    aprovadosB <- aprovadosB + 1
  fimse
  se (nota > notamaxB)
    notamaxB <- nota
    aluno_primeiro <- nome
  senao
    se (nota == notamaxB)
      aluno_primeiro <- aluno_primeiro + ", " + nome
    fimse
  fimse
fimpara

escreva("Alunos Truma C")
para x de 1 ate 2 faca
  escreva("Digite o nome do aluno:")
  leia(nome)
  escreva("Digite a nota do aluno:")
  leia(nota)
  se (nota > 7) entao
    aprovadosC <- aprovadosC + 1
  fimse
  se (nota > notamaxC)
    notamaxC <- nota
    aluno_primeiro <- nome
  senao
    se (nota == notamaxC)
      aluno_primeiro <- aluno_primeiro + ", " + nome
    fimse
  fimse
fimpara

escreva("Alunos Truma D")
para x de 1 ate 2 faca
  escreva("Digite o nome do aluno:")
  leia(nome)
  escreva("Digite a nota do aluno:")
  leia(nota)
  se (nota > 7) entao
    aprovadosD <- aprovadosD + 1
  fimse
  se (nota > notamaxD)
    notamaxD <- nota
    aluno_primeiro <- nome
  senao
    se (nota == notamaxD)
      aluno_primeiro <- aluno_primeiro + ", " + nome
    fimse
  fimse
fimpara


Fimalgoritmo