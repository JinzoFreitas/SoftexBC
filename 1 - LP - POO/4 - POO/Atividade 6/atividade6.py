# Softex - Recife
# Janderson Freitas
# Unidade 1 - Mod 4 - Atividade 6
# serialização e desserialização 

'''
Crie um exemplo de como funcionam a serialização e a desserialização de um sistema qualquer. Utilize as classes, os objetos e métodos padrões da Java e insira um endereço físico fictício.
'''

# Module Python object serialization.
import pickle

# Using the class from the previous exercise.
class MyText:

    def __init__(self, text: str) -> None:
        self.__text = text
    
    def get_text(self) -> str:
        return self.__text

    def set_text(self, new_text: str) -> None:
        self.__text = new_text

    def upper_Text(self) -> str:
        return self.__text.upper()

    def count_letter(self, letter: str, count=0) -> int:
        for i in self.__text:
            if i.lower() == letter.lower():
                count +=1 
        return count
    
    def invert_text(self) -> str:
        len_text=len(self.__text)
        inv = self.__text[len_text::-1] 
        return inv

text = MyText('Hello, my friend. you are ok? What is happned?')
print(f'\nText original object: {text.get_text()}')

# Serialized object in storage string
srlz = pickle.dumps(text)
print('\nSerialized object!')
print(f'Storage string: {srlz}')

# Object Deserialized
dsrlz = pickle.loads(srlz)
print('\nDeserialized object')
print(f'Text new object: {dsrlz.get_text()}')