#include <stdio.h>
#include <stdlib.h>

void deudBo(int n, int m, char *a, char *b);

int main() {
    int n, m;

    scanf("%d %d", &n, &m);

    char *known[n];
    *known = malloc(sizeof(char)*20);
    
    char *check[m];
    *check = malloc(sizeof(char)*20);

    for(int i=0; i<n; i++) {
        scanf("%s", &known[i]);
    }

    for(int i=0; i<m; i++) {
        scanf("%s", &check[i]);
    }

    printf("%s", known[0]);

    deudBo(n, m, known, check);

    return 0;
}

void deudBo(int n, int m, char *a, char *b) {
    int count = 0;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if(a[i] == b[j]) {
                count++;
                printf("%c\n", b[j]);
            }
        }
    }
}