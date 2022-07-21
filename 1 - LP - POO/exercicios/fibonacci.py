#Softex - Recife
#Janderson freitas
#Exercício - Fibonacci

def fibonacci(n_element):
  fib = []
  fib.append(1)
  fib.append(1)
  for i in range(2, n_element):
    fib.append(fib[(i-1)] + fib[(i-2)])
  print(f"\n\nFibonacci com {n_element} termos: ")
  return print(fib)

def main():
  print("[Gerador da Senquência de Fibonacci]")
  n_element = int(input("Informe o número de elementos da sequência: "))
  fibonacci(n_element)

main()