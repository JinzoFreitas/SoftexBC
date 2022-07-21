# Softex - Recife
# Janderson Freitas
# Unidade 1 - Mód2 - Tarefa 7

'''
1- Código desenvolvido em Python e ainda em fase de teste. 
2- Para declarar uma árvore binária em Python, crie uma classe Tree com uma função __init__() que irá instanciar esses três campos de classe: o nó filho esquerdo, o nó filho direito e os dados do nó atual. Os três campos mencionados são a composição de uma árvore binária simples.
'''
class Tree:
  def __init__(self, val = None):
    if val != None:
        self.val = val
    else:
        self.val = None 
    self.left = None
    self.right = None

# Função para inserir e comparar os novos valores,
# copara com a raiz e adiciona novo valor a direita ou esquerda do nó
  def insert(self, val):
    if self.val:
        if val < self.val:
            if self.left is None:
                self.left = Tree(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Tree(val)
            else:
                self.right.insert(val)
    else:
        self.val = val

  def printValues(self):
    if self.left:
        self.left.printValues()
    print(self.val)
    if self.right:
        self.right.printValues()

#Declarando as listas:
list1 = [45,20,30,60,81,97,100,7,8,4]
list2 = [15,6,18,3,7,16,20,4]

# Criando as árvores e recebendo o primeiro elemento da lista como raiz:
tree1 = Tree(list1[0])
tree2 = Tree(list2[0])

#Inserindo os valores da lista na Árvore:
for i in range(1,len(list1)):
    tree1.insert(list1[i])
for i in range(1,len(list2)):
    tree2.insert(list2[i])

print('Árvore da lista 1')
tree1.printValues()
print('\nÁrvore da lista 2')
tree2.printValues()