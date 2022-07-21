#include <stdio.h>
#include <stdlib.h>

int main() {

    int* ptr;
    int ptr[4];
    char valor[] = "poha";
    ptr = &valor;
    int result = soma(1, 4);

    printf("Endereco = %x\n", &valor);
    printf("Endereco = %x\n", ptr);
    printf("Valor = %s\n", *ptr);
    printf("soma = %d", result);

    return 0;
}

int soma(int a, int b)
{
    return a + b;
}