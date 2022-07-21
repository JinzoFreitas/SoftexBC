# Softex - Recife
# Janderson Freitas
# Atividade 3 - Bomb

'''
Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir. Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”. 
'''
#Código personalizado em homenagem ao CS 1.6, espero que gostem! 

import time

while True:
    temp = int(input('Digite o tempo da Bomba em segundos: '))
    print("Bomb has been planted")
    for i in range(temp,0,-1):
        print(f"{i}s")
        time.sleep(1)
    print("\nBUMMMMMMMMMMMMMMMMMMM!!!!!!")
    break
print('\nTerrorist Wins!')