n=int(input())
a=0
for i in range (n):
  x=list(map(int, input().split()))
  
 
  if x.count(1)>=2:
   a+=1
   
   
print(a)