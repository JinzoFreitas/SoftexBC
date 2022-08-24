# Softex - Recife
# Janderson Freitas
# Unidade 1 - Mod 4 - Atividade 3

'''
Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter um método acessor (get) e um método modificador (set) para cada. Defina um objeto para cada atributo e elabore um construtor para criar alguma regra.

A atividade pode ser realizada em qualquer linguagem de programação ou apenas utilizando algoritmos.
'''

class Book:
    
    def __init__(self, title: str, nPag: int) -> None:
        # Double underscore determine private attributes in class. 
        self.__title = title
        self.__nPag = nPag
 
    def get_title(self) -> str:
        '''Getter to return the title of book:'''
        return self.__title

    def set_title(self, new_title: str) -> str:
        '''Setter to new title'''
        self.__title = new_title

    def get_nPag(self) -> int:
        '''Getter to return the number of Book pages:'''
        return self.__nPag

    def set_nPag(self, new_nPag):
        '''Setter to determine the new number of pages in the book:'''
        self.__nPag = new_nPag

book1 = Book('Lord of the Rings - I', 423)
book2 = Book('The Da Vinci Code', 689)

# AttributeError: privates attributes need Getters e Setter.
# print(book1.__title)
# print(book2.__title)

print(book1.get_title())
book1.set_title('Lord of the Rings - V')
print(book1.get_title())

print(book1.get_nPag())
book1.set_nPag(530)
print(book1.get_nPag())
