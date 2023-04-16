PASSWORD = "asdfghjkl"

GRANTED = "greetings professor falcon"

DENIED = "access denied"

for i in range(3):
    guess = input("enter the password")
    
    if guess == PASSWORD:
        print(GRANTED)
        break

    else:
        print(DENIED)


