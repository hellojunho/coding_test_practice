import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
        
    i, j = 0, 0
    result = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            ans.append(left[i])
            i+=1
        else:
            result.append(right[j])
            ans.append(right[j])
            j+=1
    
    while i < len(left):
        result.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        ans.append(right[j])
        j+=1

    return result

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []
merge_sort(a)

if len(ans) >= m:
    print(ans[m-1])
else:
    print(-1)