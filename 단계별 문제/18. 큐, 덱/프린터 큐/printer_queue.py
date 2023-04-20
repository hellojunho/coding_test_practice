import sys
from collections import deque

q = deque()
n = int(sys.stdin.readline())
what = []

for i in range(n):
    num1, num2 = list(map(int, sys.stdin.readline().split()))
    what = list(map(int, sys.stdin.readline().split()))
    index = list(range(len(what)))
    index[num2] = 'target'

    order = 0
    while True:
        if what[0] == max(what):
            order += 1
            if index[0] == 'target':
                print(order)
                break
            else:
                what.pop(0)
                index.pop(0)

        else:
            what.append(what.pop(0))
            index.append(index.pop(0))