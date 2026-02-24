s = input()
t = input()
j = 0
a = 1

for i in t: 
    if i == s[j]:
        a += 1
        j += 1

print(a)