# the fridge

"""

get the user to enter a temperature in cesius

< 0: print "fridge too cold"
0 - 4: print "fridge OK"
4 - 6: print "fridge too warm"
> 6: print "fridge broken

"""

temperature = input("enter the fridge temperature: ")

temperature = float(temperature)

if temperature < 0:
    print("fridge is too cold")
elif temperature < 4:
    print("fridge is OK")
elif temperature < 6:
    print("fridge is too warm")
else:
    print("fridge is broken")