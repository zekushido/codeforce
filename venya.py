x , y = map(int , input().split())
a =list( map (int , input().split()))
b=0
for i in range (x):
    if a[i]<=y:
        b+=1
    else:
        b+=2
print (b)