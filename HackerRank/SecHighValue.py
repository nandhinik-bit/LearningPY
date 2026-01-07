# QUE 1 : SECOND HIGH VALUE
# i/p1: 5   2 3 5 6 6       o/p1: 5 
# i/p2: 4   1 2 3 4         o/p2: 3
num = int(input())
arr = map(int,input().split())
ar = set(arr)
first = float('-inf')  #float('-inf') = negative infinity, smaller than any real number.
sec = float('-inf')

for x in ar:
    if x > first:
        sec = first
        first = x
    elif x > sec:
        sec = x
print(sec)
