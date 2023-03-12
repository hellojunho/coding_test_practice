# (알고리즘 문제풀이에서) 모든 입력을 배열에 저장하면 당연히 메모리 초과 입니다.
# sort()를 사용하면 메모리초과날 확률 높음

import sys

N = int(sys.stdin.readline())

arr = [0 for _ in range(10001)]

for i in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)