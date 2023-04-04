import sys

a,b=map(int,sys.stdin.readline().split())
A,B=a,b

while a%b!=0:
    a,b=b,a%b

result = A%B/b
print(A*B//b)