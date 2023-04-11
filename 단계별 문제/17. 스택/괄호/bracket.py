import sys

def vps(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return "NO"
            stack.pop()
    if len(stack) != 0:
        return "NO"
    else:
        return "YES"

n = int(sys.stdin.readline())
result = []
for i in range(n):
    ps = input()
    check = vps(ps)
    result.append(check)
    
for i in result:
    print(i)