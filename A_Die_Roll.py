y, w = map(int, input().split())
 
h = max(y, w)
a = 6 - h + 1
 
f = ["", "1/6", "1/3", "1/2", "2/3", "5/6", "1/1"]

print(f[a])