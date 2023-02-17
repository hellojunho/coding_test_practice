def check(x):
    for i in range(x):
        if arr[x] == arr[i]:
            return False
        elif arr[x] == arr[i] or abs(arr[x] - arr[i]) == x - i:
            return False
    return True

def back_tracking(x):
    global result
    if x == n:
        result += 1
        print(arr, end='\n')

    else:
        for i  in range(n):
            arr[x] = i
            if check(x):
                back_tracking(x + 1)


n = int(input())
arr = [0] * n
result = 0

back_tracking(0)
print(result)