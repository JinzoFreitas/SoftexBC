#include <stdio.h>

void main(){
    int a = 2;
    int b = 3;
    int result;
    int* prt;
    prt = &result;

    result = testePonteiro(a, b);
    printf("%d", result);

}

int testePonteiro(int a, int b){
    return (a + b);  
}
