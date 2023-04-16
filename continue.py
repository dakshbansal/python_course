
for i in range(5):
    print("starting loop number " + str(i))

    stop = input("stop the loop (y/n) ? ")

    if stop == "y":
        continue

    print("ending loop number " + str(i))

print("program ended")