day = ""
count, aux = 0, 0   
array_day = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]

day = str(input("Digite o dia da semana: "))
count = int(input("Digite o número de dias para avançar: "))
aux = array_day.index(day)

for x in range(0, count) :
  aux = aux + 1
  if aux == 7 :
    aux = 0

print(f"Depois de {count} dias do(a) {day}, o dia será {array_day[aux]}")