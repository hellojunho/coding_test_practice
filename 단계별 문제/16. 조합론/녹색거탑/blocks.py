# block 개수 확인하는 함수
import sys

def blocks(n):
    sum = 0
    for i in range(1, n+1):
        inner_sum = 0
        for j in range(1, i+1):
            inner_sum += j
        sum += inner_sum

    return sum

n = int(sys.stdin.readline())

print(blocks(n))
