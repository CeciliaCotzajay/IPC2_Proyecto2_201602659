import webbrowser
from xml.dom import minidom


class MetodosImage:
    cadenaEscritura = ""

    def cargarArchivo(self, pahtArchivo):
        rutaArchivo = pahtArchivo
        docXML = minidom.parse(rutaArchivo)
        matrices = docXML.getElementsByTagName("matrices")[0]
        listaMatriz = matrices.getElementsByTagName("matriz")

    def mostrarDocumentacion(self):
        ruta = str("C:\\Users\\Maria\\Documents\\GitHub\\IPC2_Proyecto2_201602659\\Ensayo-Proyecto2-IPC2.pdf")
        webbrowser.open_new(ruta)

    def mostrarReporteHTML(self):
        # ---------------------------------------------------------
        # ESTA LINEA SERÁ ELIMINADA Y  SERÁ CONVERTIDA EN PARAMETRO
        nombre = "hola"
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
