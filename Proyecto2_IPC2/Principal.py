from tkinter import *
from AcerdaDe import AcercaDe


class Principal:

    raiz = Tk()
    raiz.title("Bienvenidos!")
    raiz.iconbitmap("img/i.ico")
    raiz.config(bg="#2980B9")  # #1A5276
    raiz.config(bd=25, width=700, height=400)
    raiz.config(relief="sunken")
    raiz.config(cursor="circle")

    # ----------------------------------------------------------------------------------------------------------------------
    # Frame1 = Frame(raiz)
    # Frame1.pack()
    # Frame1.config(width="500", height="350")
    # Frame1.config(bg="#2980B9")
    # Frame1.config(bd=15)
    # Frame1.config(relief="sunken")
    # Frame1.config(cursor="dot")
    def cambiarFormAcercaDe(self):
        acerca = AcercaDe()
    # ----------------------------------------------------------------------------------------------------------------------
    barraMenu = Menu(raiz)
    raiz.config(menu=barraMenu)

    archivoMenu = Menu(barraMenu, tearoff=0)
    archivoMenu.add_command(label="Cargar Archivo")
    archivoMenu.add_command(label="Reiniciar")
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Salir", command=raiz.destroy)
    archivoMenu.config(fg="#000080", bg="#808B96", font=("Comic Sans MS", 10))

    operacionesMenu = Menu(barraMenu, tearoff=0)
    operacionesMenu.add_command(label="Rotación Horizontal")
    operacionesMenu.add_command(label="Rotación Vertical")
    operacionesMenu.add_separator()
    operacionesMenu.add_command(label="Transpuesta de Imagen")
    operacionesMenu.add_command(label="Limpiar zona de Imagen")
    operacionesMenu.add_separator()
    operacionesMenu.add_command(label="Agregar línea Horizontal")
    operacionesMenu.add_command(label="Agregar línea Vertical")
    operacionesMenu.add_separator()
    operacionesMenu.add_command(label="Agregar rectángulo")
    operacionesMenu.add_command(label="Agregar Tireangulo Rectángulo")
    operacionesMenu.config(fg="#000080", bg="#808B96", font=("Comic Sans MS", 10))

    reportesMenu = Menu(barraMenu, tearoff=0)
    reportesMenu.add_command(label="Ver Reporte")
    reportesMenu.config(fg="#000080", bg="#808B96", font=("Comic Sans MS", 10))

    ayudaMenu = Menu(barraMenu, tearoff=0)
    ayudaMenu.add_command(label="Documentación")
    ayudaMenu.add_command(label="Acerca de...", command=cambiarFormAcercaDe)
    ayudaMenu.config(fg="#000080", bg="#808B96", font=("Comic Sans MS", 10))

    barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
    barraMenu.add_cascade(label="Operaciones", menu=operacionesMenu)
    barraMenu.add_cascade(label="Reporte", menu=reportesMenu)
    barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
    barraMenu.config(fg="#000080", bg="#808B96", font=("Comic Sans MS", 10))
    # ----------------------------------------------------------------------------------------------------------------------
    botonIniciar = Button(raiz, text="Iniciar!")
    botonIniciar.config(fg="Purple", bg="#808B96", font=("Comic Sans MS", 10))
    botonIniciar.place(x=310, y=300)
    botonIniciar.config(cursor="hand2")
    # ----------------------------------------------------------------------------------------------------------------------
    raiz.mainloop()

# p = Principal()
# p.VentanaPrincipal()
