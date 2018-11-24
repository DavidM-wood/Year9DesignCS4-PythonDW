import tkinter as tk 

root = tk.Tk()

labUN = tk.Label(root, text = "User Name")

labUN.pack()

entUN = tk.Entry(root)
entUN.pack(padx =10)

labPassword = tk.Label(root, text = "Password")
labPassword.pack()

entPassword = tk.Entry(root)
entPassword.pack()

btnSubmit = tk.Button(root, text = "Submit") 
btnSubmit.pack()

root.mainloop()