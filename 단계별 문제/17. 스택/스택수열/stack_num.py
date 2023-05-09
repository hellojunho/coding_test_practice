import sys

n = int(sys.stdin.readline())

stack = []
result = []
find = True
count = 1

for i in range(n):
    num = int(sys.stdin.readline())
    while count <= num:
        stack.append(count)
        result.append('+')
        count+=1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        find = False

if not find:
    print('NO')
else:
    for i in result:
        print(i)