// 백준-7568 : 덩치
// (a1, b1), (a2, b2) 일 때
// a1 > a2 && b1 > b2 -> 덩치가 크다

// 백준 코드 제출 시, 컴파일 에러 발생
#include <stdio.h>
#include <stdlib.h>

int main() {

    int N = 0;
    scanf("%d", &N);   

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

    int *count = malloc(sizeof(int)*N);

    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            if(people[i][0] < people[j][0] && people[i][1] < people[j][1])
                count[i]++;
        }
        printf("%d ", count[i]+1);
    }
    
    return 0;
}