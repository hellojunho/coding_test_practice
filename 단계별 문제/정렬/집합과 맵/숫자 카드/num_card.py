# 이분탐색은 결과값이 0/1 혹은 true/false로 나올 때 사용한다.
import sys

N = int(sys.stdin.readline())   # input 5 [6 3 2 10 -10]
cards = sorted(list(map(int, sys.stdin.readline().split())))    # -10 2 3 6 10
M = int(sys.stdin.readline())   # input 8 [10 9 -5 2 3 4 5 -10]
checks = list(map(int, sys.stdin.readline().split()))

for check in checks:
    low, high = 0, N-1
    exist = False

    while low <= high:
        mid = (low + high) // 2     # 2 -> 3 -> 4
        if cards[mid] > check:
            high = mid - 1
        elif cards[mid] < check:
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')