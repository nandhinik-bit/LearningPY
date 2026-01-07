# LIST COMPREHENSION

# [new_value for item in iterable if condition] -> MEMORY TRICK(KEY)  => FILTERING
# [ WHAT_TO_ADD  if CONDITION else WHAT_TO_ADD  for item in list ]  => (TRANSFORMATION)

#EXAMPLES 1:
n = [i*i for i in range(4)]    # for i in range(5):
print(n)                       #print(i*i)


#EXAMPLE 2:
# Sample Input 0
# 1
# 1
# 1
# 2
# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
x = int(input())
y = int(input())
z = int(input())
n = int(input())
res = [[i,j,k]
       for i in range(x+1)
       for j in range(y+1)
       for k in range(z+1)
       if i+j+k != n]
print(res)


# EXAMPLE3:
# i/p : 3   2 7 3
# o/p : ["True" , 7 ,3]
num = int(input())
ans = [
    "True" if (ar := int(input())) % 2 == 0 else ar
    for _ in range(num)
]
print(ans)

a = 100
b = 100
print(a is b)
print(a == b)


