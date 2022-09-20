c3 = 0 
c5 = 0 
d = ""
for i in range(1,100):
    c3 +=1
    c5 +=1
    if (c3==3):
        d += "Fizz"
        c3 = 0 
    if (c5 == 5):
        d += "Buzz"
        c5 = 0 
    if (d == ""):
        print(i)
    else:
        print(d)
    d = ""
