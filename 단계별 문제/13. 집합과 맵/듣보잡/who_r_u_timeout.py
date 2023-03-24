# # 시간초과 발생 코드

# import sys

# n, m = map(int, sys.stdin.readline().split())

# known = set()
# for i in range(n):
#     known.add(sys.stdin.readline().rstrip())

# check = []
# for i in range(m):
#     check.append(sys.stdin.readline().rstrip())

# result = []
# for i in known:
#     for j in check:
#         if j in i:
#             result.append(j)

# result.sort()
# print(len(result))
# for i in result:
#     print(i)