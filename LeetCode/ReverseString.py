# ip : ["h","e","l","l","o"]
# op : ["o","l","l","e","h"]
s = ["h","e","l","l","o"]
x = s
s[:] = s[::-1]

print(x)

# to get an char
# ip: hello 
# op: ['h', 'e', 'l', 'l', 'o'] 
s = input()
char = list(s)
print(s)
