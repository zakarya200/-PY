a = int(input("please entr the number a"))
b = int(input("please entre the numbre b"))
if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)