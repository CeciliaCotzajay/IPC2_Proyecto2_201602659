import webbrowser
from datetime import datetime
from select import select
from xml.dom import minidom

from Casilla import Casilla
from ListaSimple import ListaSimple
from MatrizOrtogonal import MatrizOrtogonal


class MetodosImage:
    cadenaEscritura = ""
    listaS = ListaSimple()

    def cargarArchivo(self, pahtArchivo):
        rutaArchivo = pahtArchivo
        docXML = minidom.parse(rutaArchivo)
        matrices = docXML.getElementsByTagName("matrices")[0]
        listaMatriz = matrices.getElementsByTagName("matriz")
        for matriz in listaMatriz:
            nombre = matriz.getElementsByTagName("nombre")[0]
            if self.listaS.buscarNombres(nombre):
                print("La lista con el nombre: " + nombre + " ya existe!!")
            else:
                fil = matriz.getElementsByTagName("filas")[0]
                col = matriz.getElementsByTagName("columnas")[0]
                image = matriz.getElementsByTagName("imagen")[0]
                filas = int(fil.firstChild.data)
                columnas = int(col.firstChild.data)
                imagen = str(image.firstChild.data)
                # print(imagen)
                matrizOrtogonal = MatrizOrtogonal(filas, columnas)
                lineasImagen = imagen.split('\n')
                contC = 0
                contF = 0
                for linea in lineasImagen:
                    if linea != '\n' and linea != '\t' and linea != "":
                        contF += 1
                        for c in linea:
                            if c != '\n' and c != '\t':
                                contC += 1
                                if c == "*":
                                    casilla = Casilla(contC, contF, "*")
                                    matrizOrtogonal.insertar(casilla)
                        if contC != columnas and contC != 0:
                            print("La imagen no tiene el No de columnas establecido!! " + linea + " nombre: " + str(
                                nombre.firstChild.data))
                        contC = 0
                if contF != filas:
                    print("La imagen no tiene el No de filas establecido!! " + str(nombre.firstChild.data))
                self.listaS.insertar(nombre, matrizOrtogonal)
                fecha = self.obtenerFechaHora()
                # linea = """<p>La matriz fue creada: """ + fecha+"""</p><br>"""
                #self.escribirLinea(nombre, linea)
                print(str(matrizOrtogonal.tam))
        # self.graficarMatriz()

    def graficarMatriz(self):
        actualL = self.listaS.primero
        while actualL is not None:
            # ----
            actuaY = actualL.MatrizOrtogonal.primero_Y
            actuaX = actualL.MatrizOrtogonal.primero_X
            while actuaY is not None:
                while actuaY is not None:
                    print(actuaY.Casilla.valor, end="\t")
                    actuaY = actuaY.siguiente
                print("")
                actuaY = actuaY.abajo
            # ----
            actualL = actualL.siguiente

    def mostrarDocumentacion(self):
        ruta = str("C:\\Users\\Maria\\Documents\\GitHub\\IPC2_Proyecto2_201602659\\Ensayo-Proyecto2-IPC2.pdf")
        webbrowser.open_new(ruta)

    def mostrarReporteHTML(self):
        # ---------------------------------------------------------
        # ESTA LINEA SERÁ ELIMINADA Y  SERÁ CONVERTIDA EN PARAMETRO
        nombre = "Reporte"
        # ---------------------------------------------------------
        self.crearArchivo(nombre)
        self.escribirLinea(nombre)
        webbrowser.open_new_tab("C:\\Users\\Maria\\Desktop\\" + nombre + ".html")

    def crearArchivo(self, nombre):
        archivo = open("C:\\Users\\Maria\\Desktop\\" + nombre + ".html", "w")
        archivo.close()

    def escribirLinea(self, nombre):
        lineaInicial = """<html>"""
        # ---------------------------------------------------------
        # ESTA LINEA SERÁ ELIMINADA Y  SERÁ CONVERTIDA EN PARAMETRO
        linea = """<p>Hola a todos!!! :)</p><br>"""
        # ---------------------------------------------------------
        self.cadenaEscritura += linea
        lineafinal = """</html>"""
        unificado = lineaInicial + self.cadenaEscritura + lineafinal
        archivo = open("C:\\Users\\Maria\\Desktop\\" + nombre + ".html", "a")
        archivo.write(unificado)
        archivo.close()

    def obtenerFechaHora(self):
        now = datetime.now()
        hora = now.strftime("%H:%M:%S")
        fecha = now.strftime("%d:%m:%y")
        FechaHora = "[" + fecha + " " + hora + "]"
        return FechaHora
