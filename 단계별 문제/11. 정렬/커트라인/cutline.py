import sys

n,k = map(int,input().split())

arr = []
arr = map(int, sys.stdin.readline().split())

cutline = []
cutline = sorted(arr, reverse=True)

print(cutline[k-1])