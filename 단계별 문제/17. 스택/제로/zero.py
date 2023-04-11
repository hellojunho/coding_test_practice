import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

sum = 0
for i in stack:
    sum += i

print(sum)