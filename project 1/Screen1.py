import tkinter as tk
from PIL import ImageTk, Image

def GPsubmit():
	

	#Step 1: Decide who is active
	print(var1.get())

	if var1.get() == "Player 1":

		#Step 2: Update the playerx[0] since index 0 is gp
		player1[0] = player1[0] + int(entGP.get())
		TbGP.delete(1,tk.END)
		TbGP.insert(1,player1[0])






	#print("Running")

def Asubmit():
	if var2.get() == "Player 1":

		#Step 2: Update the playerx[0] since index 0 is gp
		player1[1] = player1[1] + int(entA.get())
		TbA.delete(1,tk.END)
		TbA.insert(1,player1[1])

	#TbA.insert(2,entA.get())

def PIMsubmit():
	if var3.get() =="Player 1":

		player1[2] = player1[2] + int(entPIM.get())
		TbPIM.delete(1,tk.END)
		TbPIM.insert(1,player1[2])
		#TbPIM.insert(2,entPIM.get())

'''def Gsubmit():
	TbG.insert(2,panel.get())'''
def change():
	print ("change")
	TbGP.delete(1,tk.END)



def motion(event):
	x = event.x #x position of mouse on panel
	y = event.y #y position of mouse on panel

	print(x,",",y)

def clicked1(event):
	print("clicked1")

	


	x = event.x #x position of mouse on panel
	y = event.y #y position of mouse on panel

	print(x,",",y)

	panel.create_oval(x,y,x+10,y+10, fill = "blue")
	
	hitormiss.append(0)
	shotx.append(x)
	shoty.append(y)
	print(hitormiss)
	print(shotx)
	print(shoty)

	if var4.get() == "Player 1":


		#Step 2: Update the playerx[0] since index 0 is gp
		player1[4] = player1[4] + 1 
		TbSOT.delete(1,tk.END)
		TbSOT.insert(1,player1[4])

def clicked2(event):
	print("clicked2")

	x = event.x #x position of mouse on panel
	y = event.y #y position of mouse on panel

	print(x,",",y)
	#
	panel.create_oval(x,y,x+10,y+10, fill = "red")

	#Store data
	hitormiss.append(1)
	shotx.append(x)
	shoty.append(y)
	print(hitormiss)
	print(shotx)
	print(shoty)

	if var5.get() == "Player 1":


		#Step 2: Update the playerx[0] since index 0 is gp
		player1[3] = player1[3] + 1 #int(panel.get()
		TbG.delete(1,tk.END)
		TbG.insert(1,player1[3])

#Three lists to store data
hitormiss = [] #0 for miss, 1 for goal
shotx = []
shoty = []
#playerx = [gp,a,pm,g,son]
player1 = [0,0,0,0,0]


root = tk.Tk()


OPTIONS = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6"]

var1 = tk.StringVar(root)
var1.set(OPTIONS	[0])
var1.trace("w",change)


var2 = tk.StringVar(root)
var2.set(OPTIONS	[0])
var2.trace("w",change)

var3 = tk.StringVar(root)
var3.set(OPTIONS	[0])
var3.trace("w",change)


var4 = tk.StringVar(root)
var4.set(OPTIONS	[0])
var4.trace("w",change)

var5 = tk.StringVar(root)
var5.set(OPTIONS	[0])
var5.trace("w",change)


something = var1.get()

def clear():
	players = {
	"Player 1": "", #mapping "Player 1" to "" (nothing)
	"Player 2": "",
	"Player 3": "",
	}


	TbGP.configure(state = "normal")
	TbGP.delete("1.0", tk.END)
	TbGP.insert("1.0",players.get(something))
	TbGP.configure(state = "normal")

dropDownMenu = tk.OptionMenu(root,var1,OPTIONS[0], OPTIONS[1], OPTIONS[2], OPTIONS[3], OPTIONS[4], OPTIONS[5])
dropDownMenu.grid(row = 0, column = 0, columnspan = 2)








labTitle = tk.Label(root, text = "Input Data: ")
labTitle.grid(row = 0, column = 3, columnspan = 2)




labGP = tk.Label(root, text = "Games Played: ")
labGP.grid(row = 1, column = 3)

entGP = tk.Entry(root)
entGP.grid(row = 1, column = 4)

SubmitBtn1 = tk.Button(root, text= "Submit", command = GPsubmit)
SubmitBtn1.grid(row= 1, column = 5)



labA = tk.Label(root, text = "Assists: ")
labA.grid(row = 2, column = 3)

entA = tk.Entry(root)
entA.grid(row = 2, column = 4)

SubmitBtn2 = tk.Button(root, text= "Submit", command = Asubmit)
SubmitBtn2.grid(row= 2, column = 5)


labPIM = tk.Label(root, text = "Penalty Minutes: ")
labPIM.grid(row = 3, column = 3)

entPIM = tk.Entry(root)
entPIM.grid(row = 3, column = 4)

SubmitBtn3 = tk.Button(root, text = "Submit", command = PIMsubmit)
SubmitBtn3.grid(row = 3, column = 5)



TbGP = tk.Listbox(root)
TbGP.insert(1, "Games Played: ")
TbGP.grid(row = 1, column = 2, stick = "NESW")



TbA = tk.Listbox(root)
TbA.insert(1, "Assists: ")
TbA.grid(row = 2, column = 2, stick = "NESW")

TbPIM = tk.Listbox(root)
TbPIM.insert(1, "Penalty Minutes: ")
TbPIM.grid(row = 3, column = 2, stick = "NESW")

TbG = tk.Listbox(root)
TbG.insert(1, "Goals: ")
TbG.grid(row = 4, column = 2, stick = "NESW")

TbSOT = tk.Listbox(root)
TbSOT.insert(1, "Shots on Net: ")
TbSOT.grid(row = 4, column = 3, stick = "NESW")



path = "Hockey_Rink_2.png"

img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Canvas(root, width = 250, height = 439)
panel.create_image(0, 0, image=img, anchor=tk.NW)
panel.grid(row = 1, column = 0, rowspan = 8)

panel.bind("<Motion>",motion)
panel.bind("<Button-1>",clicked1)
panel.bind("<Button-2>",clicked2)










root.mainloop()