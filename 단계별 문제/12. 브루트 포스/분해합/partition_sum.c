#include <stdio.h>

int num_pos_sum(int num);

int main() {
    int n=0;
    scanf("%d", &n);

    int num_sum = 0;

    for(int i=1; i<n+1; i++) {
        num_sum = num_pos_sum(i) + i;

        if(num_sum == n){
            printf("%d", i);
            break;
        }
        else if(i == n)
            printf("%d", 0);
    }


    return 0;
}

int num_pos_sum(int num) {
    int t = 0;
    
    for(int i=num; i>0; i=i/10)
        t=t+i%10;

    return t;
}