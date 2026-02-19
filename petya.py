n=input().lower()
x = input().lower()
 
for i in range (len(n)):
 
    if n[i]>x[i]:
        print ("1")
        break
    elif n[i]<x[i]:
        print ("-1")
        break
    elif n==x:
        print ("0")
        break