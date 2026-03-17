
num = list(map(int, input().split()))

first = -1 #init min value
sec = -1

for i in num:
    if i > first:
        sec = first
        first = i
    elif i > sec:
        sec = i
print(sec)
