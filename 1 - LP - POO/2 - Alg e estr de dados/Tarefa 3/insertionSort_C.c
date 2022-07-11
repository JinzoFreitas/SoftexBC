#include <stdio.h>


int main(){
    int insertionSort[] = {21, 11, 47, 105, 33, 17, 9, 1, 61, 55, 3, 27, 13, 99, 19, 45, 79, 15, 51, 23, 35, 37, 111, 41, 301, 107, 63, 55, 87};
    int i, j, auxTroca;

    for (i = 1; i <= 29; i++)
    {
        auxTroca = insertionSort[i];
        j = i - 1;

        while (j >= 0 && insertionSort[j] > auxTroca)
        {
            insertionSort[j + 1] = insertionSort[j];
            j = j - 1;
        }

        insertionSort[j + 1] = auxTroca;
    }

    printf("Array organizada com insertion sorte: ");

    for (i = 0; i <= 29; i++)
    {
        printf("%d ", insertionSort[i]);
    }
}