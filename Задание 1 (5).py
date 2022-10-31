n = int(input("Введите число n: "))
t = str(n)
t1 = n ^ n
t2 = n ^ n ^ n
comt = t = int(t1) ^ int(t2)
print("Результат равен:", comt)