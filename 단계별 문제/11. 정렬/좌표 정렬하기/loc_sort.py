import sys

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])

loc = sorted(arr, key = lambda x : (x[0], x[1]))

for i in range(N):
    print(loc[i][0], loc[i][1])