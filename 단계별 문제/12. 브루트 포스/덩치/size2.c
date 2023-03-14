#include <stdio.h>

#define MAX 50

int main() {
    int N;
    scanf("%d", &N);

    int weight[MAX] = {0, };
    int height[MAX] = {0, };

    for(int i=0; i<N; i++) {
        scanf("%d %d", &weight[i], &height[i]);
    }

    int count;
    for(int i=0; i<N; i++) {
        count = 0;
        for(int j=0; j<N; j++) {
            if(weight[i] < weight[j] && height[i] < height[j])
                count++;
        }

        printf("%d ", count+1);
    }    

    return 0;
}