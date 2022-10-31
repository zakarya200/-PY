year = int(input("please entre your year"))
if   year% 4==0 and year% 100!=0 or year% 400==0 :
    print("Tall")
else :
     print ("Normal")