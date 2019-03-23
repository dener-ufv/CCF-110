#include <stdio.h>
#include <stdlib.h>

int **aloca(int size_x, int size_y) {
	int **mat;
	mat = (int **) malloc(size_y*sizeof(int *));
	for(int i=0; i<size_y; i++) {
		mat[i] = (int *) malloc(size_x*sizeof(int));
	}
	return mat;
}

void libera(int **mat, int size_x, int size_y) {
	for(int i=0; i<size_y; i++) {
		free(mat[i]);
	}
	free(mat);
}

void mostra(int **mat, int size_x, int size_y) {
	for(int i=0; i<size_y; i++) {
		for(int j=0; j<size_x; j++) {
			printf("%d    ", mat[i][j]);
		}
		printf("\n");
	}
}

void carrega(int **mat, int size_x, int size_y) {
	int sentido = 0;		// 0-direita, 1-baixo, 2-esquerda, 3-cima
	int px = 0, py = 0;	// posicão atual, x e y
	int minX = 0,
			maxX = size_x - 1,
			minY = 0,
			maxY = size_y - 1;	// minimos e maximos para percorrer

	for(int valor=1; valor <= size_x*size_y; valor++) {
		mat[py][px] = valor;
		switch(sentido) {
			case 0:
				if(px < maxX) {
					px++;
				} else {
					sentido = 1;
					py++;
					minY++;
				}
				break;

			case 1:
				if(py < maxY) {
					py++;
				} else {
					sentido = 2;
					px--;
					maxX--;
				}
				break;

			case 2:
				if(px > minX) {
					px--;
				} else {
					sentido = 3;
					py--;
					maxY--;
				}
				break;

			case 3: 
				if(py > minY) {
					py--;
				} else {
					sentido = 0;
					px++;
					minX++;
				}
				break;

			default: ;
		}
	}
	

}

int main() {
	int **matriz;
	int tamanho_x;
	int tamanho_y;

	printf("tamanho da matrix (x,y)\n");
	printf("X: ");
	scanf("%d", &tamanho_x);
	printf("Y: ");
	scanf("%d", &tamanho_y);

	matriz = aloca(tamanho_x, tamanho_y);
	carrega(matriz, tamanho_x, tamanho_y);
	mostra(matriz, tamanho_x, tamanho_y);
	libera(matriz, tamanho_x, tamanho_y);
	
	return 0;
}
