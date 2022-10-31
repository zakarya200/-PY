a = int(input("please entre the number a:"))
b = int(input("please entre the number b:"))
c = int(input("please entre the number c:"))
d = int(input("please entre the number d:"))
x=a%2
y=b%2
z=c%2
f=d%2
if x==1 and y==1 and z==1 and f==1:
    print("yes")
elif x==1 and y==1 and z==0 and f==0:
    print("yes")
elif x==0 and y==0 and z==1 and f==1:
    print("yes")
elif x==1 and y==0 and z==1 and f==0:
    print("yes")
elif x==0 and y==1 and z==0 and f==1:
    print("yes")
elif x==1 and y==1 and z==0 and f==1:
    print("No")
elif x==1 and y==1 and z==1 and f==0:
    print("No")
elif x==0 and y==0 and z==1 and f==0:
    print("No")
elif x==0 and y==0 and z==0 and f==1:
    print("No")
elif x==1 and y==0 and z==1 and f==1:
    print("No")
elif x==1 and y==0 and z==0 and f==1:
    print("No")
elif x==0 and y==1 and z==0 and f==0:
    print("No")
elif x==1 and y==0 and z==0 and f==1:
    print('YES')
else:
    print("No")