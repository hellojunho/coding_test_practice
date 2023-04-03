# 시간초과 발생 코드

# import sys

# setNum = int(input())

# num = [[0] * 2] * setNum
# for i in range(setNum):
#     num[i] = list(map(int, sys.stdin.readline().split()))

# for x in range(setNum):
#     for i in range(max(num[x][0], num[x][1]), (num[x][0] * num[x][1]) + 1):
#         if i%num[x][0] == 0 and i%num[x][1]==0:
#             print(i)
#             break