print("*********************************************************************")

print("0")
print("1")
print("2")
print("3")

#When we think of a for loop I want you think about 
#Count: The variable that holds the current count
#Check: The check that is done each time the loop runs
#Change: The change applied to the count each time the loop run

#for <count var> in range (<inital value>, <check value>, <change>):
print("********************************")
#i = 0, 0 < 4, True RUN LOOP
# i = 1, 1 < 4, True RUN LOOP
# i = 2, 2 < 4, True RUN LOOP
# i = 3, 3 < 4, True RUN LOOP
# i = 4, 4 < 4, False EXIT AND CONTINUE.


for i in range(0,4,1):
	print(i)


print("*********************************")
#Change the loop parameters so it prints -44 to 136 inclusive 

for i in range(-44, 137, 1):
	print (i)
	if (i % 2 == 0):
		print(str(i)+" is even")
	else:
		print(str(i)+"is odd")