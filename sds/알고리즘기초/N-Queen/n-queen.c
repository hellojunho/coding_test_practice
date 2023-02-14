#include <stdio.h>

int is_correct_pos(int row, int col, int* col_arr) {
    for (int i = 0; i < row; i++) {
        if (col_arr[i] == col) {
            return 0;
        }
        if ((i + col_arr[i] == row + col) || (i - col_arr[i] == row - col)) {
            return 0;
        }
    }
    return 1;
}

void n_queens(int n, int iter, int* col_arr, int* ans) {
    if (iter == n) {
        *ans += 1;
        for (int i = 0; i < n; i++) {
            printf("%d", col_arr[i]);
        }
        printf("\n");
        return;
    }
    for (int col = 0; col < n; col++) {
        if (is_correct_pos(iter, col, col_arr)) {
            col_arr[iter] = col;
            n_queens(n, iter + 1, col_arr, ans);
        }
    }
}

int ft_n_queens_puzzle(int n) {
    int col_arr[20];
    int ans = 0;
    n_queens(n, 0, col_arr, &ans);
    return ans;
}

int main() {
    int set;

    scanf("%d", &set);
    printf("%d\n", ft_n_queens_puzzle(set));
}