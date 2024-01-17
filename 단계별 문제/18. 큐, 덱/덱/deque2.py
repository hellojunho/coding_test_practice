import sys
from collections import deque

input = sys.stdin.readline
d = deque()
n = int(input())

for i in range(n):
    s = input().split()
    s1 = s[0]

    if s1=='push_back':
        d.append(s[1])
    elif s1=='phsh_front':
        d.appendleft(s[1])
    elif s1=='front':
        print(d[0])
        d.popleft()
    elif s1=='back':
        print(d[-1])
        d.pop()
    elif s1=='size':
        print(len(d))
    elif s1=='empty':
        if len(d)==0:
            print(1)
        else:
            print(0)

for i in d:
    print(i, end='')