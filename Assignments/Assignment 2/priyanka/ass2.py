import random
temp = random.randint(10,50)#16 - 40
humi = random.randint(1, 100)#40-low   max-70
if(temp<20):
    print("temperature is low and the temperature is"+temp)
elif(temp>35):
    print("temperature is high and the temperature is"+temp)
if(humi<40):
    print("low humidity and the humidity is %s"+""+humi)
elif(humi>65):
    print("high humidity the humidity is"+humi)