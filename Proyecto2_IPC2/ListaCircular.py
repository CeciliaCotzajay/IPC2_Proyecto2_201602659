from NodoCircular import NodoCircular


class ListaCircular:

    def __init__(self):
        self.primero = None
        self.tam = 0

    def insertar(self, noombre, matrizOrto):
        nuevo = NodoCircular(nombre=noombre, MatrizOrtogonal=matrizOrto)
        if self.tam == 0:
            self.primero = nuevo
            self.primero.siguiente = self.primero
            self.tam += 1
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.primero
            # primero = nuevo
            self.tam += 1

    def imprimirNormal(self):
        if self.tam == 0:
            print("----->La lista esta Vacia")
            return
        else:
            actual = self.primero
            print(actual.nombre, end=" => ")
            while actual.siguiente != self.primero:
                actual = actual.siguiente
                print(actual.nombre, end=" => ")