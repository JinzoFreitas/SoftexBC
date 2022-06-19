#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void imprimir();
int i, aux, troca, numero[5];
int main()
{
    setlocale(LC_ALL, "Portuguese");
    printf("\n--------------------------------------------");
    printf("\nEXEMPLO BUBBLE SORT CRESCENTE");
    printf("\n--------------------------------------------");
    printf("\nInicializando o Array");
    for(i=0; i<5; i++)
    {
        numero[i] = 0;
    }
    imprimir();
    printf("\n--------------------------------------------");
    printf("\nInserindo valores no Array\n");
    for(i=0; i<5; i++)
    {
        printf("\n|Posição %d |Digite um número: \t", i);
        scanf("%d%*c",&numero[i]);
    }
    printf("\n--------------------------------------------");
    printf("\nValores armazenados no array");
    imprimir();
    printf("\n--------------------------------------------");
    printf("\nOrdenando o Array");
    troca = 1;
    while (troca == 1)
    {
        troca = 0;        
        for (i = 0; i <= 3; i++)
        {
            if (numero[i] > numero[i + 1])
            {
                troca = 1;
                aux = numero[i];
                numero[i] = numero[i + 1];
                numero[i + 1] = aux;
            }
        }
    }
    printf("\n--------------------------------------------");
    printf("\nValores ordenados");
    imprimir();
    printf("\n--------------------------------------------");
    return 0;
}
 
void imprimir()
{
    printf("\n--------------------------------------------");
    for (i=0; i<5; i++)
    {
        printf("\n|Posicao: %d | Número: %d|", i, numero[i]);
    }
}