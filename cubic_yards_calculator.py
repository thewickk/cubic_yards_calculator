lengthInFeet = 0.0
widthInFeet = 0.0
depthInInches = 0.0



while True:

    while True:
        try:
            lengthInFeet = float(input("Please enter the number of FEET in the LENGHT of your project: \n"))
            if float(lengthInFeet):
                break
        except ValueError:
            print("Please enter a numerical value. Ex 55.2 - \n")
            continue
    while True:
        try:
            widthInFeet = float(input("Please enter the number of FEET in the WIDTH of your project: \n"))
            if float(widthInFeet):
                break
        except ValueError:
            print("Please enter a numerical value. Ex 55.2 - \n")
            continue
    while True:
        try:
            depthInInches = float(input("Please enter the number of INCHES in the DEPTH of your project: \n"))
            if float(depthInInches):
                break
        except ValueError:
            print("Please enter a numerical value. Ex 55.2 - \n")
            continue

    confirm = input("You have entered a length of {} feet, a width of {} feet, and a depth of {} inches.\n"
                    "\nPlease enter \"yes\" if this is correct or \"no\" to edit your input: "
                    .format(lengthInFeet, widthInFeet, depthInInches)).lower()


    while True:
        if confirm == "yes" or confirm == "no":
            break
        else:
            confirm = input("Please enter \"yes\" or \"no\": ")
            continue

    if confirm == "yes":
        break
    if confirm == "no":
        continue
        print()

def calculateCubiFeet(length, width, depth):
    inchesToFeet = depth / 12
    cubicFeetVolume = (length * width * inchesToFeet)
    return cubicFeetVolume


def calculateCubicYards(length, width, depth):
    inchesToFeet = depth / 12
    cubicVolume = ((length * width * inchesToFeet) / 27)
    return cubicVolume

print()
print("Your project will require %.3f cubic feet of material." % (calculateCubiFeet(lengthInFeet, widthInFeet,
                                                                  depthInInches)))
print()
print("***NOTE*** Most supply companies sell material in cubic yards. See next result for cubic yards")
print()


print("Your project will require %.3f cubic yards of material." % (calculateCubicYards(lengthInFeet, widthInFeet,
                                                             depthInInches)))
