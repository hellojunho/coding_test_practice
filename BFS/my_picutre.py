import sys
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    result = 1
    q = deque()
    q.append((y, x))



input = sys.stdin.readline()

n, m = map(int, input.split())

picture = list()
picture.append(map(int, input.split()) for _ in range(n))

check = [[False] * m for _ in range(n)]