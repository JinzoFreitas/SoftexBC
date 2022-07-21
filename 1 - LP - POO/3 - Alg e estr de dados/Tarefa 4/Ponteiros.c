#include <stdio.h>
#include <stdlib.h>

void main(){

    // Ponteiro do tipo inteiro
    int *ptr;

    // ptr recebe o endereço do primeiro elemento do vetor
    ptr = (int *) malloc(10 * sizeof (int)); 

    //ptr recebe o endereço de memória do novo vetor agora com 22 elementos
    ptr = (int *) realloc(ptr , 22 * sizeof ( int));

    //Libera o espaço de memória alocada para 'ptr'
    free(ptr);

    return 0;
}