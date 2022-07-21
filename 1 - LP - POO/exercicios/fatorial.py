#Softex - Recife
#Janderson Freitas
#Exercício - Fatorial


def fat(x) -> int:
  if (x == 0):
    return 1
  else:
    return x*fat(x-1)

def main():
  print("Calculadora Fatorial (!)")
  num = int(input("Digite um valor para calcular seu fatorial: "))
  resp = fat(num)
  print(f"\n{num}! = {resp}")


main() 