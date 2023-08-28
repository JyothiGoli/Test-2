# b=[1, 4, 2, 5, 3, 7]
n=int(input())
b=[]
for i in range(0,n):
    x=int(input())
    b.append(x)
x=int(input())
s=[]
l=[]
w=[]
for i in range(0,len(b)):
    if x>b[i]:
        s.append(b[i])
    elif x<b[i]:
        l.append(b[i])
w.append(s)
w.append(l)
print(w)
