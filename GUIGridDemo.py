import tkinter as tk
root = tk.Tk()   #Tk( ) is a special method called a constructor 
				#A constructor is a special method only called once
				#It sets everything up for us.










lab = tk.Label(root, text = "Enter a number:")
#To back an element using the grid geometry mamnger. We use
#<object>.grod(<parameters>)


lab.grid(row = 0, column = 0)

ent = tk.Entry(root)
ent.grid(row = 1, column = 0)

btn = tk.Button(root)
ent.grid(row = 2, column = 0)

output = tk.Text(root)
output.configure(state = "disable", bg = "black")
output.grid(row = 0, column = 1 , rowspan= 3 )



root.mainloop()