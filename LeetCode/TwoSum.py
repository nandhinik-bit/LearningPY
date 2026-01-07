# ip: nums = [2,7,11,15]  target = 9  
# 0p: [0,1]
nums = list(map(int,input().split()))
target = int(input())
ans = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            ans = [i]+[j]
print(ans)