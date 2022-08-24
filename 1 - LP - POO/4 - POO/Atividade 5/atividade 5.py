# Softex - Recife
# Janderson Freitas
# Manipular strings

'''
Estruture três códigos, os quais devem conter uma função de manipulação de string que obtenha resultado.
'''

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

print(text.count_letter('e'))
print(text.count_letter(' '))
print(text.get_text())
print(text.upper_Text())
print(text.invert_text())

text.set_text("I'm fine, I was sick, but now I'm feeling better!")
print(text.count_letter('e'))
print(text.count_letter('i'))
print(text.get_text())
print(text.upper_Text())
print(text.invert_text())
