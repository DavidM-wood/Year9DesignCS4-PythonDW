fName = input ("What is your first name? ")
lName = input ("What is your last nanme? ")


result = fName[0] + "." + lName 

lenfName = len(fName)
lenlName = len(lName)

codeName = fName[0] + fName[-1] + "." + lName[0] + lName[-1]
#codeName = fName[0] + fName[len(fName)-1]

print ("Hi " + result)

print ("your code name is:" + codeName)