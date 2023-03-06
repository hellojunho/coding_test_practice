import sys

a = []
for i in range(0, 5):
    num = int(sys.stdin.readline())
    a.append(num)
sum = 0
for i in range(0, 5):
    sum += a[i]

arr = sorted(a)
print(round(sum/5))

# center = round((0 + 5) / 2)
# print(arr[center])
print(arr[2])