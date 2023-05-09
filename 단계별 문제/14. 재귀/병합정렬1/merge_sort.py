import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i = j = 0
    result = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            result.append(right[j])
            ans.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    ans.append(result)
    
    
    return result
    
n,m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

ans = []
res = merge_sort(a)

if len(ans) >= m:
    print(res[m%len(res)])
else:
    print(-1)