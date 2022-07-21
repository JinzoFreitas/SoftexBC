# Softex - Recife
# Janderson Freitas
# Atividade 3 - Bomb

'''
Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir. Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”. 
'''
#Código personalizado em homenagem ao CS 1.6, espero que gostem! 


# Importa a biblioteca time para poder usar no programa
import time

# Recebe o tempo em segundos do contador
temp = int(input('Digite o tempo da Bomba em segundos: '))
print("\nBomb has been planted")

# Repetição para contagem regressiva da bomba
for i in range(temp,0,-1):

    # Imprimi os segundos restantes na tela
    print(f"{i}s")

    # A linha espera 1 segundo antes de prosseguir
    time.sleep(1)

print("\nBUMMMMMMMMMMMMMMMMMMM!!!!!!")
print('\nTerrorist Wins!')