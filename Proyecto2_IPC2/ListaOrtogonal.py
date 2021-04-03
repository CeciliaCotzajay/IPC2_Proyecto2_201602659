from NodoOrtogonal import NodoOrtogonal


class ListaOrtogonal:

    def __init__(self):
        self.primero = None
        self.tam = 0

    def insertarY(self, idn):
        nuevo = NodoOrtogonal(iD=idn)
        if self.tam == 0:
            self.primero = nuevo
            self.tam += 1
        else:
            actual = self.primero
            while actual is not None:
                actual = actual.abajo
            actual.abajo = nuevo
            nuevo.arriba = actual
            self.tam += 1

    def insertarX(self, idn):
        nuevo = NodoOrtogonal(iD=idn)
        if self.tam == 0:
            self.primero = nuevo
            self.tam += 1
        else:
            actual = self.primero
            while actual is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
            self.tam += 1

    def obtenerCabeceraY(self, valY):
        cabeceraY = None
        if self.tam != 0:
            actual = self.primero
            while actual is not None:
                if actual.iD == valY:
                    cabeceraY = actual
                actual = actual.abajo
        return cabeceraY

    def obtenerCabeceraX(self, valX):
        cabeceraX = None
        if self.tam != 0:
            actual = self.primero
            while actual is not None:
                if actual.iD == valX:
                    cabeceraX = actual
                actual = actual.siguiente
        return cabeceraX

    def imprimirNormal(self):
        if self.tam == 0:
            print("----->La lista esta Vacia")
            return
        else:
            actual = self.primero
            while actual is not None:
                print(actual.nombre, end=" => ")
                actual = actual.siguiente