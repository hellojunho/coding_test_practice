import sys

N = int(input())

a = []
for i in range(N):
    n = int(sys.stdin.readline())
    a.append(n)

arr = sorted(a)
for i in range(N):
    print(arr[i])