import sys
input = sys.stdin.readline

N, M = map(int, input().split())

setStr = set()
for i in range(N):
    setStr.add(input())

count = 0
for _ in range(M):
    inputStr = input()
    if inputStr in setStr:
        count += 1

print(count)