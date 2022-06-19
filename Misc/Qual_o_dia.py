
count, aux, day, month, year = 0, 0, 0, 0, 0   
array_day = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
dic_month = {"Janeiro":31,
             "Fevereiro":28,
             "Março":31,
             "Abril":30,
             "Maio":31,
             "Junho":30,
             "Julho":31,
             "Agosto":31,
             "Setembro":30,
             "Outubro":31,
             "Novembro":30,
             "Dezembro":31}

normal_year = 365

day = int(input("Digite o Dia: "))
month = str(input("Digite o Mês: "))
year = int(input("Digite o Ano: "))


aux = array_day.index(day)
for x in range(0, count) :
  aux = aux + 1
  if aux == 7 :
    aux = 0

print(f"Depois de {count} dias do(a) {day}, o dia será {array_day[aux]}") 