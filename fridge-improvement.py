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

STATUS_BROKEN = "fridge is broken"
STATUS_OK = "fridge is OK"
STATUS_COLD = "fridge is too cold"
STATUS_WARM = "fridge is too warm"

status = STATUS_BROKEN

if temperature < 0:
    status = STATUS_COLD
elif temperature <= 4:
    status = STATUS_OK
elif temperature < 6:
    status = STATUS_WARM

print(status)