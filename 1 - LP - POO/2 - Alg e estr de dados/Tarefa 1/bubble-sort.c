/*
Softex - Recife
Aluno: Janderson Freitas
Algoritmo BubbleSort
*/


void BubbleSort(int vetor[], int tamanho){
	int memoria, troca, i, j;
	troca = 1; 
	for(j=tamanho-1; (j>=1) && (troca==1); j--){
		troca=0; /*Se o valor continuar 0 na próxima passada quer dizer que não houve troca e a função é encerrada.*/
		for(i=0; i<j; i++){
				if(vetor[i]>vetor[i+1]){
					memoria = vetor[i];
					vetor[i] = vetor[i+1];
					vetor[i+1] = memoria;
					troca=1; /*Se houve troca, "troca" recebe 1 para continuar rodando.*/
			}
		}
	}
}

void main(){
    
    int n, i;
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &n);
    int vetor[n];
    for(i=0; i<n; i++){
        printf("Digite o valor da posicição %d: ", i);
        scanf("%d", &vetor[i]);
    }
	
    BubbleSort(vetor,n);

	for(i=0; i<n; i++){
    	printf("%d\n", vetor[i]);
	}
}