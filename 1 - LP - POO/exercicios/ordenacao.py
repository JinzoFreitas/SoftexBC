# Softex
# Janderson Freitas
# Ordenação de vetores

def main():
  vetor = []
  aux = 0
  for i in range(10):
    vetor.append(int(input("Digite um valor para o vetor: ")))
  
  print("Vetor inicial:")
  print(vetor)  
  
  for i1 in range(9):
    for i2 in range(i1+1,10):
      if (vetor[i2] < vetor[i1]):
        aux = vetor[i2]
        vetor[i2] = vetor[i1]     
        vetor[i1] = aux    
  
  print("Vetor ordenado:")
  print(vetor)    

main()