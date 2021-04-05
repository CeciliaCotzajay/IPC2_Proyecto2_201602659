from NodoOrtogonalMatriz import NodoOrtogonalMatriz


class ListaOrtogonal:

    def __init__(self):
        self.primeroY = None
        self.primeroX = None
        self.tamY = 0
        self.tamX = 0
        self.tamG = 0

    def insertarCabeceraY(self, casilla):
        nuevo = NodoOrtogonalMatriz(Casilla=casilla)
        if self.tamY == 0:
            self.primeroY = nuevo
            self.tamY += 1
            self.tamG += 1
        else:
            actual = self.primeroY
            while actual.abajo:
                actual = actual.abajo
            actual.abajo = nuevo
            nuevo.arriba = actual
            self.tamY += 1
            self.tamG += 1

    def insertarCabeceraX(self, casilla):
        nuevo = NodoOrtogonalMatriz(Casilla=casilla)
        if self.tamX == 0:
            self.primeroX = nuevo
            self.tamX += 1
            self.tamG += 1
        else:
            actual = self.primeroX
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
            self.tamX += 1
            self.tamG += 1

#
    def obtenerCabeceraY(self, valY):
        cabeceraY = None
        if self.tamY != 0:
            actualY = self.primeroY
            while actualY.abajo:
                if actualY.Casilla.posY == valY and actualY.Casilla.posX == 0:
                    cabeceraY = actualY
                actualY = actualY.abajo
        return cabeceraY

    def obtenerCabeceraX(self, valX):
        cabeceraX = None
        if self.tamX != 0:
            actualX = self.primeroX
            while actualX.siguiente:
                if actualX.Casilla.posX == valX and actualX.Casilla.posY == 0:
                    cabeceraX = actualX
                actualX = actualX.siguiente
        return cabeceraX

    def imprimirNormal(self):
        if self.tamG == 0:
            print("----->La lista esta Vacia")
            return
        else:
            actual = self.primero
            while actual is not None:
                print(actual.nombre, end=" => ")
                actual = actual.siguiente