a = int(input("please entre the number"))
b = int(input("pleasr entre the number"))
for i in range(a-(a+1)%2,b+b%2, -2):
    print(i, end=' ')