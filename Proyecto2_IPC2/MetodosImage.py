import webbrowser


class MetodosImage:
    cadenaEscritura = ""

    def mostrarReporteHTML(self):
        nombre = "hola"
        self.crearArchivo(nombre)
        self.escribirLinea(nombre)
        webbrowser.open_new_tab("C:\\Users\\Maria\\Desktop\\" + "hola" + ".html")

    def crearArchivo(self, nombre):
        archivo = open("C:\\Users\\Maria\\Desktop\\" + nombre + ".html", "w")
        archivo.close()

    def escribirLinea(self, nombre):
        self.cadenaEscritura = """
        <html>
        <p>Hola a todos!!! :)</p>
        </html>
        """
        archivo = open("C:\\Users\\Maria\\Desktop\\" + nombre + ".html", "a")
        archivo.write(self.cadenaEscritura + '\n')
        archivo.close()
