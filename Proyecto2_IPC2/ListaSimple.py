from NodoSimple import NodoSimple


class ListaSimple:

    def __init__(self):
        self.primero = None
        self.tam = 0

    def insertar(self, noombre, matrizOrto):
        nuevo = NodoSimple(nombre=noombre, MatrizOrtogonal=matrizOrto)
        if self.tam == 0:
            self.primero = nuevo
            self.tam += 1
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo
            self.tam += 1

    def imprimirNormal(self):
        if self.tam == 0:
            print("----->La lista esta Vacia")
            return
        else:
            actual = self.primero
            while actual is not None:
                print(actual.nombre, end=" => ")
                actual = actual.siguiente
