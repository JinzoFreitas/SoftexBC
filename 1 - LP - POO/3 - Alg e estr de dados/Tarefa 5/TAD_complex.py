# Softex - Recife
# Janderson Freitas
# Tarefa 5

'''
Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
O método deve:

- calcular três números complexos;
- realizar todas as operações básicas;
- e imprimir as propriedades real e img do números.
'''

class myComplexo:
    def __init__(self, real, imag, result = 0):
        self.real = real
        self.imag = imag*1j
        self.result = self.real + self.imag
        print(
            f'Número: {self.result}\n' 
            f'- Parte real: {self.real}\n'
            f'- Parte imaginária: {self.imag}\n'
        )
    def soma(a, b, c):
        A = a.result
        B = b.result
        C = c.result
        return print(f'Resultado da Soma dos três números igual a: {(A+B)+C}')
    def sub(a, b, c):
        A = a.result
        B = b.result
        C = c.result
        print(f'Resultado da Subtração dos três números igual a: {(A-B)-C}')
    def mult(a, b, c):
        A = a.result        
        B = b.result
        C = c.result       
        return print(f'Resultado da multiplicação sucessiva dos três números: {(A*B)*C}')
    def div(a, b, c):
        A = a.result        
        B = b.result
        C = c.result       
        return print(f'Resultado da multiplicação sucessiva dos três números: {(A/B)/C:.2}')

x = myComplexo(1,4)
y = myComplexo(2,1)
z = myComplexo(4,3)

print(myComplexo.soma(x , y, z))
print(myComplexo.sub(x, y, z))
print(myComplexo.mult(x , y, z))
print(myComplexo.div(x, y, z))
