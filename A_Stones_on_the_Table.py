x = int(input())
z = input()
s = 0

for i in range(1, x):
    if z[i] == z[i-1]:
        s += 1

print(s)