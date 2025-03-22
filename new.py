from tkinter import * 

window = Tk()

window.geometry("500x500")
window.configure(background = "Lightgreen")

'''#using pack method
l1 = Label(window, text = "Hello World", bg = "pink", fg = "magenta", padx = 20, pady = 20)
l1.pack(padx = 20,pady = 20)

e1 = Entry(window)
e1.pack()

b1 = Button(window, text = "Click Here",bg = "Black", fg = "White")
b1.pack()

window.mainloop()

#Using grid method
l1 = Label(window, text = "Hello World", bg = "pink", fg = "magenta", padx = 20, pady = 20)
l1.grid(row = 0, column = 0)

e1 = Entry(window)
e1.grid(row = 0, column = 1)

b1 = Button(window, text = "Click Here",bg = "Black", fg = "White")
b1.grid(row = 1, column = 1, columnspan = 2)

e2 = Entry(window)
e2.grid(row = 1, column = 3)
window.mainloop()'''

#Using place method
l1 = Label(window, text = "Hello World", bg = "pink", fg = "magenta", padx = 20, pady = 20)
l1.place(x = 50, y = 50)

e1 = Entry(window)
e1.place(x = 200, y = 200)

b1 = Button(window, text = "Click Here",bg = "Black", fg = "White")
b1.place(x = 150, y = 150)


window.mainloop()