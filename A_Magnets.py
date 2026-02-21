x = int(input())
a=1
k=[5]
for i in range(x):
  y = input()
  if k[-1] != y[0]:
    k.append(y[1])
  else:
    a+=1  
    k.append(y[1])
print(a)