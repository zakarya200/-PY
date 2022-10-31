x = 3 ; y =5
x , y = int(input("x=")), int(input("y="))
print(f"before x={x}, y={y}")
s = x
x = y
y = s
print(f"after x={x}, y={y}")