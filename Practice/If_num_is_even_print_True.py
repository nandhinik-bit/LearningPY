# i/p : 3   2 7 3
# o/p : ["True" , 7 ,3]
num = int(input())
ans = []
for i in range(num):
    ar = int(input())
    if ar % 2 == 0:
        ans.append("True")
    else:
        ans.append(ar)
        
print(ans)