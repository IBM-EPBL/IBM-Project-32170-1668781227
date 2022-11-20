import random as r 
t=r.randint(15,50)
h=r.randint(0,100)
if t in range(15,25):
    print("low temperature:"+t)
elif t in range(25,35):
    print("normal temperature"+t)
else:
    print("high temperature")
if h in range(0,40):
    print("low humidity"+h)
elif h in range(40,70):
    print("normal humidity"+h)
else:
    print("high humidity"+h)