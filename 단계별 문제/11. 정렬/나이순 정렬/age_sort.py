import sys

N = int(sys.stdin.readline())

user = []

for i in range(N):
    user.append(list(input().split()))

user.sort(key=lambda a:int(a[0]))

for i in range(N):
    print(user[i][0], user[i][1])