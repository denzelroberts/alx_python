import random
number = random.randint(-10000, 10000)
lastnumber = str(number)
lastnumber = lastnumber[-1]
lastnumber = int(lastnumber)
text = "Last digit of "


if lastnumber > 5:
    print(str(text), number, "is", lastnumber, "and is greater than 5")

if lastnumber < 6 and lastnumber == 0:
    print(str(text), number, "is", lastnumber, "and is 0")

if lastnumber < 6:
    print(str(text), number, "is", lastnumber, "and is less than 6 and not 0")