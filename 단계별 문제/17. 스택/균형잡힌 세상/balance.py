# 틀린코드긴 함..

import sys

def vps(ps):
    stack = []
    
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack)!=0 and stack[-1] == '(':
                stack.pop()
        elif char == '[':
            stack.append(char)

        elif char == ']':
            if len(stack)!=0 and stack[-1] == '[':
                stack.pop()

    if len(stack) != 0:
        return "NO"
    else:
        return "YES"

result = []

for i in range(7):
    ps = input()
    check = vps(ps)
    result.append(check)
    
for i in result:
    print(i)