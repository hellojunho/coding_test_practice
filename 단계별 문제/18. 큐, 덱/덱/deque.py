import sys
from collections import deque

q = deque()
n = int(sys.stdin.readline())

for i in range(n):
    string = sys.stdin.readline().split()
    string_str = string[0]

    if string_str == 'push_front':
        q.appendleft(string[1])

    elif string_str == 'push_back':
        q.append(string[1])

    elif string_str == 'pop_front':
        if q:
            print(q[0])
            q.popleft()
        else:
            print(-1)
    elif string_str == 'pop_back':
        if q:
            print(q[-1])
            q.pop()
        else:
            print(-1)
    elif string_str == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif string_str == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif string_str == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif string_str == 'size':
        print(len(q))
