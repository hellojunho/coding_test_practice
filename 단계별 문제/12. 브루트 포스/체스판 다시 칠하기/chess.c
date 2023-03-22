#include <stdio.h>
#include <stdlib.h>

char chess[52][52];

int main() {

    int N, M;
    scanf("%d %d", &N, &M);

    char **chess;
    chess = malloc(sizeof(char*)*N);
    for(int i=0; i<N; i++) {
        chess[i] = malloc(sizeof(char)*M);
    }

    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++)
            scanf("%s", &chess[i][j]);

    for(int i=0; i<N; i++) {
        for(int j=0; j<M; j++) {
            printf("%c", chess[i][j]);
        }
    }

    return 0;
}