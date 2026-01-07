# ip : ["h","e","l","l","o"]
# op : ["o","l","l","e","h"]
s = ["h","e","l","l","o"]
x = s
s[:] = s[::-1]
print(x)