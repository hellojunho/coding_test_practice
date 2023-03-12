#include <stdio.h>
#include <stdlib.h>

int main() {
    int N = 0;

    scanf("%d", &N);
    // N입력 조건 -> 위반 시 종료
    if(2>N || N>50)
        return 0;        

    // 2차원 배열 동적 할당
    int **people;
    people = (int**)malloc(sizeof(int*)*N);
    for(int i=0; i<N; i++) {
        people[i] = (int*)malloc(sizeof(int)*2);
    }

    // 입력 받음
    for(int i=0; i<N; i++) {
            scanf("%d %d", &people[i][0], &people[i][1]);
    }

    

    return 0;
}