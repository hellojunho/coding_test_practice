import sys

n, m = list(map(int, sys.stdin.readline().split()))

known = set()
for i in range(n):
    known.add(sys.stdin.readline().rstrip())

check = set()
for i in range(m):
    check.add(sys.stdin.readline().rstrip())

result = set()
count = 0
for i in known:
    for j in check:
        if j in i:
            result.add(j)
            count += 1


print(count)
for i in result:
    print(i)