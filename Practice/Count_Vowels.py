#3.COUNT VOWELS
n = input()
count = 0
for ch in n or ch in "AEIOU":
    if ch in "aeiou":
        count += 1
print(count)
