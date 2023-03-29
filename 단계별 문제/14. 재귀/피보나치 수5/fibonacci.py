# F_n = F_n-1 + F_n-2 (n>=2)
import sys

input = sys.stdin.readline

def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))