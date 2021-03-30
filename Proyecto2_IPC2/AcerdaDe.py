from tkinter import *


class AcercaDe:
    raizAcer = Tk()
    raizAcer.title("Bienvenidos!")
    raizAcer.iconbitmap("img/i.ico")
    raizAcer.config(bg="purple")
    raizAcer.config(bd=25)
    raizAcer.config(relief="groove")
    raizAcer.config(cursor="circle")
    # ----------------------------------------------------------------------------------------------------------------------
    Frame1 = Frame(raizAcer)
    Frame1.pack()
    Frame1.config(width="610", height="350")
    Frame1.config(bg="#2980B9")
    Frame1.config(bd=15)
    Frame1.config(relief="sunken")
    Frame1.config(cursor="dot")
    # ----------------------------------------------------------------------------------------------------------------------
    fondo = PhotoImage(file="img/image1.gif")
    fondo0 = fondo.subsample(2)
    # ----------------------------------------------------------------------------------------------------------------------
    label1 = Label(Frame1, image=fondo0)
    label1.place(x=30, y=20)
    Label(Frame1, text="Introducción a la Programación y Computación 2", justify="center", bg="#D2B4DE",
          font=("Comic Sans MS", 10)).place(x=275, y=70)
    Label(Frame1, text="Sección E", fg="Purple", bg="#D5F5E3", font=("Comic Sans MS", 11)).place(x=380, y=125)
    Label(Frame1, text="María Cecilia Cotzajay López", bg="#D2B4DE", font=("Comic Sans MS", 10)).place(x=330, y=175)
    Label(Frame1, text="201602659", fg="Purple", bg="#D5F5E3", font=("Comic Sans MS", 11)).place(x=370, y=230)
    # ----------------------------------------------------------------------------------------------------------------------
    botonIniciar = Button(raizAcer, text="Cerrar", command=raizAcer.withdraw)  # , command=self.cerrarForm)
    botonIniciar.config(fg="Purple", bg="#808B96", font=("Comic Sans MS", 10))
    botonIniciar.place(x=250, y=300)
    botonIniciar.config(cursor="hand2")
    #
    # ----------------------------------------------------------------------------------------------------------------------
    raizAcer.mainloop()
# acerca = AcercaDe()
