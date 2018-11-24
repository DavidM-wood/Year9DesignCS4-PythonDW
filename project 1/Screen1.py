import tkinter as tk


def change():
	print ("change")
root = tk.Tk()


OPTIONS = ["Player 1", "Player 2", "Player 3"]

var = tk.StringVar(root)
var.set(OPTIONS	[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var,OPTIONS[0], OPTIONS[1], OPTIONS[2])
dropDownMenu.grid(row = 0, column = 0, columnspan = 2)

canvas = tk.Canvas(root, height = 300, width = 200, background = "black")
canvas.grid(row = 1, column = 0, columnspan = 2)

submitBtn = tk.Button(root,text = "Submit")
submitBtn.grid(row = 2, column = 0)

rapidBtn = tk.Button(root, text = "Rapid")
rapidBtn.grid(row = 2, column =1)


stats = tk.Text(root, height = 10, width = 40, background = "green")
stats.grid(row = 1, column = 2, stick = "NESW")

sortBtn = tk.Button(root, text = "Low to High")
sortBtn.grid(row =2, column = 2, sticky = "NESW")

root.mainloop()