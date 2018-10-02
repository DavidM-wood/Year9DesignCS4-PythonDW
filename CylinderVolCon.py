import math

print("This program calculates the volume of")
print("a cylinder given radius and height")

r = input("what is the radius: ")
r = float(r)

h = input("what is the height: ")
h = float(h)

v = math.pi*r*r*h
v = round(v,3)


print("Given")
print(" radius = ",r," units")
print(" height = ",h," units")
print("The volume is: ",v," units cubed")

print("END PROGRAM")
