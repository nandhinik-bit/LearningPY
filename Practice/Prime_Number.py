# PRIME NUMBER  : 2 3 5 7 11....
# ip: 2   op: True
n = int(input())
if n <= 1:
    print("False")

else:
    for i in range(2,n):
        if n % i == 0:
            print("False")
            break
    else: 
        print("True")