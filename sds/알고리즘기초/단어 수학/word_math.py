# 아스키코드: A: 65 ~ Z: 90

s = int(input())

arr = []
for i in range(s):
    str = input()

    for i in str:
        if i =='A':
            i = 9
            arr.append(i)
        if i=='B':
            i = 4
            arr.append(i)
print(arr)