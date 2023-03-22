# 이분탐색은 결과값이 0/1 혹은 true/false로 나올 때 사용한다.
import sys
from collections import Counter

n = sys.stdin.readline().rstrip()
numSet = list(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline().rstrip()
checkSet = list(map(int, sys.stdin.readline().split()))

count = Counter(numSet)

for i in range(len(checkSet)):
    if checkSet[i] in count:
        print(count[checkSet[i]], end=' ')
    else:
        print(0, end=' ')