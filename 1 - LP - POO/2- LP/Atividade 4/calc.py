# Softex - Recife
# Janderson Freitas
# Atividade 4 - Calc



'''
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
'''

def calc(num1, num2, opera):

    if (opera == 1):
        result = num1+num2
        return result        
    elif (opera == 2):
        result = num1-num2
        return result 
    elif (opera == 3):
        result = num1*num2
        return result 
    elif (opera == 4):
        if (num2 == 0):
            print('MathError! Não é possível dividir por zero.')
            return None
        else:
            result = num1/num2
            return result 
    else:
        return 0        

# Laço para tratamento de erro com retorno infinito:
# o programa só vai rodar após uma entrada válida de dados!
while True:
        try:
            num1 = (float(input('Digite o Primeiro número: ')))
            num2 = (float(input('Digite o Segundo número: ')))
            print("Escolha uma operação a seguir:")
            print('1 - Adição;\n2 - Subtração;\n3 - Multiplicação;\n4 - Divisão.')
            opera = (int(input(f'Digite o número da operação escolhida: ')))
            break
        except ValueError:
            print('Valor inválido, tente novamente!\n')


resultado = calc(num1,num2,opera)
print(f'\nResultado da operação igual a {resultado:.2f}')            
