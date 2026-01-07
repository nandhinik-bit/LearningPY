# 2. Missing Values
# i/p: 6    1 2 4 6
# op : [3 ,5]
n = int(input())
arr = list(map(int,input().split()))
missing = []

for i in range(1,n+1):
    if i not in arr:
        missing.append(i)
print(missing)  