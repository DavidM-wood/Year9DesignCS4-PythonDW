#A loop is a programjnf structure that can repeat a section of code.
#A loop can run the same coede exactly over and over or 
#with domr yhought it can generate a patter

#There are two borad catagories of loops 
#Conditional loops: These loop as long as a conditon is true

#Counted Loops (for): These loop usikng a counter to keep teack of how many the loop has run






# you can use any loop in any situation,but usually from a design 
#perspectie there is a better loop in terms of coding
#If you know in advance how many times a loop should run a COUNTED LOOP \
#is usually the better choice.

#If you don't know how many times a loop should run a CONDITIONAL LOOP 
#is usually the better choice


print("**************************************************************************")
#TAKING INPUTS 

word = "" #We have to declaire and inialize word so it fails the while loop
#A while loop evaluates a condition when it is first reached.while
#If the condition is true it enters the loop block
while len(word) <6 or word.isalpha() == False:
	#Loop block
	word = input("Please input a word longer than 5 letters: ")


	if len(word) <6:
		print("Buddy, I said more than 5 letters ")
	if (word.isalpha() == False):
		print("Buddy I said a real word")

	#When we reach the bottom of the loop block we check the condtion 
	#again. If it is true, we g back to the top of the block and run it again
print(word+" is a seriosly long word!")
#CAUTION: DO NOT USE WHILE LOOPS TO CONTROL INPUT WITH GUI PROGRAMS



