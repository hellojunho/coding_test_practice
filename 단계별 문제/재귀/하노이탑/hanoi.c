#include <stdio.h>
#include <stdlib.h>

void hanoi(int n);

int main() {
    int plate;
    scanf("%d", &plate);

    int **result;
    result = (int **)malloc(sizeof(int*)*3);
    for(int i=0; i<3; i++) {
        result[i] = (int*)malloc(sizeof(int)*3);
    }

    return 0;
}