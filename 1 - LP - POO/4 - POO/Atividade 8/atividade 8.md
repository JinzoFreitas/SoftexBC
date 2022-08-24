# Softex - Recife
# Janderson Freitas
## Unidade 1 - Mod 4 - Atividade 8
___

### Escolha e descreva um padrão de projeto

___

## Prototype

É um tipo de padrão de projeto que se enquadra na categoria de padrão Criaciona, onde possibilita a criação de novos objetos a partir de um modelo original ou protótipo que é clonado.

Este padrão pode ser utilizado para:

- Evitar que as subclasses que criam objetos funcionem como o padrão abstract factory;
- Evitar criar um novo objeto utilizando a palavra new, o que diminui o custo de memória.
- Basicamente, ao em vez de o cliente implementar um código que utiliza o operador new, este utiliza o método clone() presente no protótipo e o método de uma fábrica(Factory Method ou Abstratct Factory) que fica encarregada de clonar o novo objeto.