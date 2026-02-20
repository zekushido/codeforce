x= input()
y=x.upper()
u=0
l=0
for i in range (len(x)):
  if x[i]==y[i]:
    u+=1
  else:
    l+=1
if u>l:
  print(y)
else: print(x.lower())