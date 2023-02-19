#include <stdio.h>

int main(void)
{
    int N = 0;
    scanf("%d", &N);

    int data[N];
    int i, j, temp = 0;


    int data_size = sizeof(data) / sizeof(int);

    for(int i=0; i<data_size; i++){
        scanf("%d", &data[i]);
    }

    for (i = 0; i < data_size; i++) {
        for (j = 0; j < (data_size - 1) - i; j++) {
            if (data[j] > data[j + 1]) {	// 버블 정렬 사용
                temp = data[j];
                data[j] = data[j + 1];
                data[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < data_size; i++) {
        printf("%d \n", data[i]);
    }

    return 0;
}