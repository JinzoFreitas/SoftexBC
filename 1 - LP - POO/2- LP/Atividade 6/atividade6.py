# Softex - Recife
# Janderson Freitas
# Atividade 6 - Calc_2

'''
Instruções do projeto
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar. 

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
'''

# Parte operacional da função, onde encontram-se os cálculos. 
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
            err_zero = '\nErro de divisão! Não é possível dividir por zero.'
            return err_zero
        else:
            result = num1/num2
            return result 
    else:
        err_opera = '\nErro de operação, certifique-se de escolher uma operação válida'
        return err_opera    

# Laço para tratamento de erro com retorno infinito:
# o programa só vai rodar após uma entrada válida de dados!
# e só vai finalizar após o comando pré-definido.
def main_calc():
    while True:
        try:
            print("\nEscolha uma operação a seguir:")
            print("1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair")
            opera = (int(input(f'Digite o número da operação escolhida: ')))

            # Condição para fim do programa.
            if opera == 0:
                print('\nFim do Programa')
                # Saída do laço e fim da execução do main()
                break
            # Entrada dos dados para operação.
            num1 = (float(input('Digite o Primeiro número: ')))
            num2 = (float(input('Digite o Segundo número: ')))

            # Resultado da calculadora.
            resultado = calc(num1,num2,opera)
            
            # Verificador de retorno, se calc() retornar str é pq houve erro no processo de operação,
            # Então o programa só vai retonar a mensagem pura.
            # Caso não seja, imprimi a mensagem de chamada padrão para o resultado padrão da operação.
            if type(resultado) != str:
                print(f'\nResultado da operação é igual a {resultado}')
            else:
                print(resultado)    
             
        # Mensagem do tratamento de Erro de entrada.
        except:
            print('\nValor inválido, tente novamente!')       

main_calc()
