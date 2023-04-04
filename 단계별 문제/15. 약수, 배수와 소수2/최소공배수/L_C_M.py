import sys

setNum=int(input())

for i in range(setNum):
    a,b=map(int,sys.stdin.readline().split())
    A,B=a,b

    while a%b!=0:
        a,b=b,a%b

    result = A%B/b
    print(A*B//b)