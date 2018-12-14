#This program was built by David Wood but Lucas Timusk helped. 

import tkinter as tk



root = tk.Tk()
def BigFont(*args):
	global p
	p += 1 
	if p%2==0:
		entDATA.config(font = ("Helvetica", 20))
		bigButton.config(text = "Smaller Font")

	else: 
		entDATA.config(font = ("Helvatica", 14))
		bigButton.config(text = "Larger Font")


BigFontbtn = tk.Button(root, text = "zoom", command = BigFont)
BigFontbtn.grid(row = 1, column = 1)



root.mainloop()