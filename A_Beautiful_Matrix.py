for i in range(5):
  x= list(map(int , input().split()))
  for j in range(5):
    if x[j] == 1: 
      c,r = i,j
print(abs(2-c)+abs(2-r))