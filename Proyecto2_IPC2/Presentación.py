from tkinter import *

raiz = Tk()
raiz.title("Bienvenidos!")
raiz.config(bg="blue")
raiz.config(bd=25)
raiz.config(relief="groove")
raiz.config(cursor="circle")
Frame1 = Frame()
Frame1.pack()
Frame1.config(width="500", height="350")
Frame1.config(bg="#A3E4D7")
Frame1.config(bd=15)
Frame1.config(relief="sunken")
Frame1.config(cursor="dot")

raiz.mainloop()