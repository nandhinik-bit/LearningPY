# ip: 121   op: True
# ip: -121  op: False
# METHOD - 1
n = int(input())
x = n 
rev = 0

while n > 0:
    dig = n % 10   #last 1
    rev = rev * 10 + dig
    n //= 10

if rev == x:
    print("True")
else:

    print("False")

# METHOD - 2
n = int(input())
cast = str(n)
rev = cast[::-1]
if rev == cast:
    print("True")
else:
    print("False)
