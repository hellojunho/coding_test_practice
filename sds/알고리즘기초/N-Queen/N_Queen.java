import java.util.Scanner;

// N-Queen
// 1. 퀸과 인접한 칸에는 다른 퀸이 있으면 안됨 -> 검사 필요
// 2. 안전한 곳에 퀸 배치

public class N_Queen {
    public static void main(String[] args) {
        int N;
        int[] cols;
        Scanner scanner = new Scanner(System.in);
        System.out.print("");
        N = scanner.nextInt();
        cols = new int[N];

        Queen queen = new Queen(N, cols);
        for (int i = 0; i < N; i++) {
            queen.back_tracking(i);
        }
    }
}

class Queen {
    int N;
    int cols[];

    public Queen(int n, int[] cols) {
        N = n;
        this.cols = cols;
    }

    public void back_tracking(int level) {

        if (level == N) {
            for (int i = 0; i < N; i++) {
                System.out.print(cols[i]);
            }
            System.out.println();
        } else {
            for (int i = 0; i < N; i++) {
                cols[level]=i;
                if (isPossible(level)) {
                    back_tracking(level+1);
                }
            }
        }
    }

    public boolean isPossible(int level) {
        for (int i = 0; i < level; i++) {
            if (cols[i] == cols[level] || Math.abs(level - i) == Math.abs(cols[level] - cols[i])) {
                return false;
            }
        }
        return true;
    }
}