import tkinter as tk
from tkinter import ttk
#Group Functions up here
def change():
	print("Change")



def clickedA():
	print("clicked")
	
	btnStat1.config(state = "disabled")
	btnStat2.config(state = "normal")
	btnStat3.config(state = "normal")

def clickedB():
	print("clicked")
	
	btnStat1.config(state = "normal")
	btnStat2.config(state = "disabled")
	btnStat3.config(state = "normal")

def clickedC():
	print("clicked")
	
	btnStat1.config(state = "normal")
	btnStat2.config(state = "normal")
	btnStat3.config(state = "disabled")

def clickedR():
	print("Clicked R")

#Group Data Variables here!
names = ["Paul", "Francesco","Stephanie","Bill","Connor","Jihoo"]
stat1 = [1,2,3,4,5,6]
stat2 = [6,5,4,3,2,1]
stat3 = [1,3,2,5,4,6]






root = tk.Tk()




output = tk.Text(root, background = "#ffd0aa", height = 10, width = 50, font = ("Helvitica",16))
#output.config(state = "disable")
output.grid(row = 0, column = 0, columnspan = 2)

#**********Configure Output Data
for i in range(0,len(names),1):
	value = names[i] + "\t"+str(stat1[i])+"\t"+str(stat2[i])+"\t"+str(stat3[i])+"\n"
	output.insert(tk.END,value)



btnStat1 = tk.Button(root, text = "Stat 1", height = 2, width = 10, command = clickedA)
btnStat1.config(state = "disabled")
btnStat1.grid(row = 1, column =0, sticky = "NESW")

btnStat2 = tk.Button(root, text = "Stat 2", height = 2, width = 10, command = clickedB)
btnStat2.grid(row = 2, column =0, sticky = "NESW")

btnStat3 = tk.Button(root, text = "Stat 3", height = 2, width = 10, command = clickedC)
btnStat3.grid(row = 3, column =0, sticky = "NESW")

MODES = [
("Ascending", "1"),
("Descending", "2")
]

v = tk.StringVar() #v keeps track of which button is selected. 
v.set("L") # initialize

for r in range(0,len(MODES),1):
	b = ttk.Radiobutton(root, text=MODES[r][0], variable=v, value=MODES[r][1], command = change)
	b.grid(row = 1 + r, column = 1, sticky = "W", padx = 40)

btnReduce = tk.Button(root, text = "Reduce Data", height = 2, width = 10, command = clickedR)
btnReduce.grid(row = 3, column = 1, sticky = "NESW")
root.mainloop()