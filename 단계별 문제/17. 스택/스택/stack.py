# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys

set = int(sys.stdin.readline())

stack = []

for _ in range(set):
    order = sys.stdin.readline().split()
    order_str = order[0]

    if order_str=='push':
        order_num = order[1]
        stack.append(order_num)
    elif order_str == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order_str == 'size':
        print(len(stack))
    elif order_str == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order_str == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])