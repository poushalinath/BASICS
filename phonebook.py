numberb_of_entries = int(input(6))
print("Okay , give me name and number respectively for each of them in order")
file = open("numbers.txt","w")
for i in range (0,6):
    name = input("Name: ")
    number = input("Number: ")
    entry = f"{name}: {number},"
    file.write(entry)
    if i == 5:
        print("Done!")
    elif i == 4:
        print("Okay next please!")
    elif i == 3:
        print("Okay next please!")
    elif i == 2:
        print("Okay next please!")
    elif i == 1:
        print("Okay next please!")
    else:
        print("Okay next please!")
file.close()