#include <stdio.h>

int fac(int num) {
    if(num == 1) {
        return 1;
    }
    else {
        return num * fac(num - 1);
    }
}

int main() {
    int num;

    scanf("%d", &num);

    printf("%d", fac(num));

    return 0;
}