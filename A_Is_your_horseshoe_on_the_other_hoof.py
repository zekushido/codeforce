x= list(map(int,input().split()))

a=[x[0]]
b=0
for i in range (3):
  if x[i+1] in a:
     b+=1
  
  else:    
    a.append(x[i+1])
   

  
   
print(b )