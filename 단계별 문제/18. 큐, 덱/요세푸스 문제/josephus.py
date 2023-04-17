import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
result= []
arr = [i for i in range(1,N+1)] 
num = 0
for i in range(N):
    num+=(K-1)
    if num >= len(arr):
        num %= len(arr)

    result.append(str(arr.pop(num)))
print("<",', '.join(result),">", sep="")