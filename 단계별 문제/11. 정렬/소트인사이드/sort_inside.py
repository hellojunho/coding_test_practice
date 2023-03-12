num = int(input())
 
arr = []
arr = list(map(int, str(num)))
    
arr.sort(reverse=True) # 내림차순 -> reverse=False가 디폴트
 
for i in arr:
    print(i, end='')