# Softex
# Janderson Freitas
# Ordenação de vetores

def main():
  vetor = []
  menor_valor = 0
  for i in range(10):
    vetor.append(int(input("Digite um valor para o vetor: ")))
  
  print(vetor)  
  
  for i1 in range(9):
    menor_valor = vetor[i1]
    for i2 in range(i1+1,10):
      if (vetor[i2] < menor_valor):
        menor_valor = vetor[i2]
        vetor[i2] = vetor[i1]     
        vetor[i1] = menor_valor    
  print(vetor)    

main()