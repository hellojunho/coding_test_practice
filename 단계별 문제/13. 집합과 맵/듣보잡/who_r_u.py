import sys

n, m = list(map(int, sys.stdin.readline().split()))

known = set()
for i in range(n):
    known.add(sys.stdin.readline().rstrip())

check = set()
for i in range(m):
    check.add(sys.stdin.readline().rstrip())

# print(known)
# print(check)

print('\n')
count = 0
result = list
for i in known:
    for j in check:
        if j in i:
            count += 1
            result.append(j)

print(count)
print(j)            