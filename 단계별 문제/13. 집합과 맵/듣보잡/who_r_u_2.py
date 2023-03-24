# python - 'in' 연산자의 시간 복잡도 
# list, tuple -> 평균 O(n)
# set, dictionary -> 평균 O(1)

import sys

n, m = map(int, sys.stdin.readline().split())

known = dict()
result = []

for i in range(n):
    x = sys.stdin.readline()
    if x not in known:
        known[x] = i


for i in range(m):
    y = sys.stdin.readline()
    if y in known:
        result.append(y)

result.sort()
print(len(result))
print(''.join(result), end='')