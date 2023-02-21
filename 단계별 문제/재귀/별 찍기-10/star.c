#include <stdio.h>

void star(int i, int j, int num);

int main() {

    int n;
    scanf("%d", &n);
    
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            star(i, j, n);
        }
        printf("\n");
    }
    
    return 0;
}

void star(int i, int j, int num) {

    if((i / num)%3==1 && (j / num)%3==1) {
        printf(" ");
    }
    else {
        if(num / 3 == 0)
            printf("*");
        else
            star(i,j,num/3);
    }
}