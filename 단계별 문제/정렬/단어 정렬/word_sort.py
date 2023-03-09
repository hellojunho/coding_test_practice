import sys

N = int(sys.stdin.readline())

words = []
for i in range(N):
    words.append(sys.stdin.readline().strip())

words = list(set(words))
words.sort()
# 문자열 길이 순 정렬
words.sort(key = len)

for i in words:
    print(i)