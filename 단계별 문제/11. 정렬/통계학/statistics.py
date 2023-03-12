import sys
from collections import Counter

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)

arr.sort()

# 산술평균
print(round(sum(arr)/N))

# 중앙값
print(arr[N//2])

# 최빈값
counted_arr = Counter(arr).most_common(2)
if N>1:
    if counted_arr[0][1] == counted_arr[1][1]:
        print(counted_arr[1][0])
    else:
        print(counted_arr[0][0])
else:
    print(counted_arr[0][0])

# 범위
print(max(arr) - min(arr))