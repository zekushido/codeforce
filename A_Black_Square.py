a = list(map(int, input().split()))
s = input()

z = 0
for i in s:
    # Convert character to int and subtract 1 to get the correct index
    x= int(i) - 1
    z += a[x]

print(z)