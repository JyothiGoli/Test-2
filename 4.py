# a=[1, 1, 1, 2, 2, 3, 4, 5, 5]
n=int(input())
a=[]
for i in range(0,n):
    x=int(input())
    a.append(x)
a=list(set(a))
print(a)