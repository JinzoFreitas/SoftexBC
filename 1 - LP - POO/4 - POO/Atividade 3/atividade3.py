#
#

'''
Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter um método acessor (get) e um método modificador (set) para cada. Defina um objeto para cada atributo e elabore um construtor para criar alguma regra.

A atividade pode ser realizada em qualquer linguagem de programação ou apenas utilizando algoritmos.
'''

class Test():
    
    @property
    def __init__(self, value):
        self._x = value

    
    def get_value(self):
        '''Getter to return the value of x:'''
        return self._x

    def set_value(self, sv):
        '''Setter to new value of x'''
        self._x = sv

test = Test(10)
print(f'value of object: {test._x}') 

val = int(input('Enter number: '))
test.set_value(val)