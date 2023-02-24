// N(3<=N<=100), M(10<=M<=300000)
// 최대한 M과 가깝게 만든다

#include <stdio.h>

int blackjack(int N, int M, int *cards);

int main() {
    
    // N(뽑는 카드의 수)
    // M(맞춰야 하는 카드의 숫자 합)
    int N, M;
    scanf("%d %d", &N, &M);

    if(3>N || N>100 || 10>M || M>300000) {
        printf("범위 오류");
        return 0;
    }

    // 책상에 놓여진 카드
    int cards[N];
    for(int i=0; i<N; i++) {
        scanf("%d", &cards[i]);
    }

    blackjack(N, M, cards);

    return 0;
}

int blackjack(int N, int M, int *cards){
    int result = 0;
    int sum = 0;
    int check = 0;
    
    for(int i=0; i<N-2; i++) {
        for(int j=i+1; j<N-1; j++) {
            for(int k=j+1; k<N; k++) {
                sum = cards[i] + cards[j] + cards[k];
                if(sum > result && sum <= M)
                    result = sum;
            }
        }
    }
    printf("%d", result);

    return result;
}