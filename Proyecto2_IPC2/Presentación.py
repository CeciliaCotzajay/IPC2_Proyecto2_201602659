from tkinter import *
from tkinter import filedialog, messagebox

from MetodosImage import MetodosImage

raizPre = Tk()
M = MetodosImage()


# **********************************************************************************************************************
# ***************************************** MÉTODOS AUXILIARES *********************************************************
# **********************************************************************************************************************

def verHTML():
    M.mostrarReporteHTML()


def verDocumentacion():
    M.mostrarDocumentacion()


def abrir_cargarArchivo():
    # try:
    rutaFichero = filedialog.askopenfilename(title="Abrir Archivo", initialdir="C:\\Users\\Maria\\Desktop",
                                             filetypes=(
                                                 ("Ficheros XML", "*.xml"), ("Todos los ficheros", "*.*")))
    print(rutaFichero)
    M.cargarArchivo(rutaFichero)
    # except:
    #     messagebox.showinfo("Abrir Archivo", "No ha Elegido ningún Archivo...")


# **********************************************************************************************************************
# ***************************************** INTERFAZ GRÁFICA ***********************************************************
# **********************************************************************************************************************

def abrirVentanaPrincipal():
    raizPre.withdraw()
    raiz = Toplevel()
    raiz.title("Bienvenidos!")
    raiz.iconbitmap("img/i.ico")
    raiz.config(bg="#2980B9")  # #1A5276
    raiz.config(bd=25, width=700, height=400)
    raiz.config(relief="sunken")
    raiz.config(cursor="circle")
    # ----------------------------------------------------------------------------------------------------------------------
    frameP = Frame(raiz)
    frameP.pack()
    frameP.config(width="600", height="300")
    frameP.config(bg="#2980B9")
    frameP.config(bd=4)
    frameP.config(cursor="hand2")
    # ----------------------------------------------------------------------------------------------------------------------
    barraMenu = Menu(raiz)
    raiz.config(menu=barraMenu)

    archivoMenu = Menu(barraMenu, tearoff=0)
    archivoMenu.add_command(label="Cargar Archivo", command=abrir_cargarArchivo)
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
    reportesMenu.add_command(label="Ver Reporte", command=verHTML)
    reportesMenu.config(fg="#000080", bg="#808B96", font=("Comic Sans MS", 10))

    ayudaMenu = Menu(barraMenu, tearoff=0)
    ayudaMenu.add_command(label="Documentación", command=verDocumentacion)
    ayudaMenu.add_command(label="Acerca de...", command=abrirVentanaAcercaDe)
    ayudaMenu.config(fg="#000080", bg="#808B96", font=("Comic Sans MS", 10))

    barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
    barraMenu.add_cascade(label="Operaciones", menu=operacionesMenu)
    barraMenu.add_cascade(label="Reporte", menu=reportesMenu)
    barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
    barraMenu.config(fg="#000080", bg="#808B96", font=("Comic Sans MS", 10))
    # ------------------------------------------------------------------------------------------------------------------
    Label(frameP, text="IPC - 2", bg="#D2B4DE", font=("Comic Sans MS", 20)).place(x=270, y=20)

    img01 = PhotoImage(file="img/image1.gif")
    img1 = img01.subsample(2)
    labeli1 = Label(frameP, image=img1, width=150, height=150)
    labeli1.place(x=30, y=90)

    img02 = PhotoImage(file="img/image1.gif")
    img2 = img02.subsample(2)
    labeli2 = Label(frameP, image=img2, width=150, height=150)
    labeli2.place(x=222, y=90)

    img03 = PhotoImage(file="img/image1.gif")
    img3 = img03.subsample(2)
    labeli3 = Label(frameP, image=img3, width=150, height=150)
    labeli3.place(x=415, y=90)
    # ----------------------------------------------------------------------------------------------------------------------
    raiz.mainloop()
    raizPre.destroy()


def abrirVentanaAcercaDe():
    raizAcer = Toplevel()
    raizAcer.title("Bienvenidos!")
    raizAcer.iconbitmap("img/i.ico")
    raizAcer.config(bg="purple")
    raizAcer.config(bd=25)
    raizAcer.config(relief="groove")
    raizAcer.config(cursor="circle")
    # ----------------------------------------------------------------------------------------------------------------------
    FrameAD = Frame(raizAcer)
    FrameAD.pack()
    FrameAD.config(width="610", height="350")
    FrameAD.config(bg="#2980B9")
    FrameAD.config(bd=15)
    FrameAD.config(relief="sunken")
    FrameAD.config(cursor="dot")
    # ----------------------------------------------------------------------------------------------------------------------
    fondo1 = PhotoImage(file="img/image1.gif")
    fondo2 = fondo1.subsample(2)
    # ----------------------------------------------------------------------------------------------------------------------
    label1 = Label(FrameAD, image=fondo2)
    label1.place(x=30, y=20)
    Label(FrameAD, text="Introducción a la Programación y Computación 2", justify="center", bg="#D2B4DE",
          font=("Comic Sans MS", 10)).place(x=275, y=70)
    Label(FrameAD, text="Sección E", fg="Purple", bg="#D5F5E3", font=("Comic Sans MS", 11)).place(x=380, y=125)
    Label(FrameAD, text="María Cecilia Cotzajay López", bg="#D2B4DE", font=("Comic Sans MS", 10)).place(x=330, y=175)
    Label(FrameAD, text="201602659", fg="Purple", bg="#D5F5E3", font=("Comic Sans MS", 11)).place(x=370, y=230)
    # ----------------------------------------------------------------------------------------------------------------------
    botonAcercaDe = Button(raizAcer, text="Cerrar", command=raizAcer.destroy)
    botonAcercaDe.config(fg="Purple", bg="#808B96", font=("Comic Sans MS", 10))
    botonAcercaDe.place(x=250, y=300)
    botonAcercaDe.config(cursor="hand2")
    #
    # ----------------------------------------------------------------------------------------------------------------------
    raizAcer.mainloop()


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
botonIniciar = Button(raizPre, text="Iniciar!", command=abrirVentanaPrincipal)
botonIniciar.config(fg="Purple", bg="#808B96", font=("Comic Sans MS", 10))
botonIniciar.place(x=250, y=300)
botonIniciar.config(cursor="hand2")
# ----------------------------------------------------------------------------------------------------------------------
raizPre.mainloop()
