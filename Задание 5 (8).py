n = int(input("please entre the number n"))
b = 0
while n!=0:
    a = int(input("please entre the numbre a"))
    if a!=0 and n < a:
        b += 1
        n = a
print(b)
