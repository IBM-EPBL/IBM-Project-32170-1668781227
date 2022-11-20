import random as r 
t=r.randint(15,50)
h=r.randint(0,100)
if t < 25:
    print("low temperature:"+t)
else:
    print("high temperature")
if h <40:
    print("low humidity"+h)
elif h >70:
    print("high humidity"+h)
