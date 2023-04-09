# 29_C_13 = 67863915
# 결국 n_C_r 을 구하는 문제

import sys

def m_C_n(n, m):
    up = 1
    down = 1

    for i in range(m, m-n, -1):
        up *= i
    for i in range(1, n+1):
        down *= i
    
    return round(up/down)
        
num = int(sys.stdin.readline())
result = []
for i in range(num):
    n, m = map(int, sys.stdin.readline().split())  

    result.append(m_C_n(n, m))

for i in range(num):
    print(result[i])