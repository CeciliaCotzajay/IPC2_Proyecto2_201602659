from tkinter import *

from Principal import Principal


class Presentacion:
    raizPre = Tk()
    raizPre.title("Bienvenidos!")
    raizPre.iconbitmap("img/i.ico")
    raizPre.config(bg="purple")
    raizPre.config(bd=25)
    raizPre.config(relief="groove")
    raizPre.config(cursor="circle")
    # ----------------------------------------------------------------------------------------------------------------------
    Frame1 = Frame(raizPre)
    Frame1.pack()
    Frame1.config(width="500", height="350")
    Frame1.config(bg="#2980B9")
    Frame1.config(bd=15)
    Frame1.config(relief="sunken")
    Frame1.config(cursor="dot")
    # ----------------------------------------------------------------------------------------------------------------------
    fondo = PhotoImage(file="img/image1.gif")
    fondo0 = fondo.subsample(2)
    # ----------------------------------------------------------------------------------------------------------------------
    label0 = Label(Frame1, image=fondo0)
    label0.place(x=30, y=20)
    Label(Frame1, text="IPC - 2", fg="Purple", bg="#D2B4DE", font=("Comic Sans MS", 20)).place(x=315, y=70)
    Label(Frame1, text="Proyecto 2 ", bg="#D5F5E3", font=("Comic Sans MS", 12)).place(x=318, y=125)
    Label(Frame1, text="1S-2021", fg="Purple", bg="#D2B4DE", font=("Comic Sans MS", 12)).place(x=330, y=175)

    # ----------------------------------------------------------------------------------------------------------------------
    def cambiarForm(self):
        self.raizPre.withdraw()
        principal = Principal()

    # ----------------------------------------------------------------------------------------------------------------------
    botonIniciar = Button(raizPre, text="Iniciar!", command=cambiarForm)
    botonIniciar.config(fg="Purple", bg="#808B96", font=("Comic Sans MS", 10))
    botonIniciar.place(x=250, y=300)
    botonIniciar.config(cursor="hand2")
    #
    # ----------------------------------------------------------------------------------------------------------------------
    raizPre.mainloop()

# ini = Presentacion()
