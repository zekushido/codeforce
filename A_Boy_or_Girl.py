x= input()
a=[]
c=0
for i in x:
  if i not in a:
    a.append(i)
    c+=1
if c%2==0:
  print("CHAT WITH HER!")
else:  print("IGNORE HIM!")