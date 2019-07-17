    
u,h=input().split()
w=abs(len(h)-len(u))
for i in range(len(u)):
    if(len(h)==1 and v[i] in u):
        break
    if(u[i]!=v[i]):
        w=w+1
print(w)
