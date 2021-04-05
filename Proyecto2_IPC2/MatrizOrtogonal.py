from Casilla import Casilla
from ListaOrtogonal import ListaOrtogonal
from NodoOrtogonalMatriz import NodoOrtogonalMatriz


class MatrizOrtogonal:

    def __init__(self, f=None, c=None):
        self.primero_X = None
        self.primero_Y = None
        self.tamFil = f
        self.tamCol = c
        self.tam = 0
        self.Matriz = None
        self.crearCabeceras()

    def crearCabeceras(self):
        self.Matriz = ListaOrtogonal()
        if self.tamFil != 0:
            contf = 1
            while contf <= self.tamFil:
                casilla = Casilla(0, contf, "")
                self.Matriz.insertarCabeceraY(casilla)
                contf += 1
        else:
            print("El número de filas es 0")
        if self.tamCol != 0:
            contc = 1
            while contc <= self.tamCol:
                casilla = Casilla(contc, 0, "")
                self.Matriz.insertarCabeceraX(casilla)
                contc += 1
        else:
            print("El número de columnas es 0")
        self.primero_X = self.Matriz.primeroX
        self.primero_Y = self.Matriz.primeroY

    def insertar(self, casilla):
        valY = casilla.posY
        valX = casilla.posX
        nuevo = NodoOrtogonalMatriz(Casilla=casilla)
        primeroY = self.Matriz.obtenerCabeceraY(valY)
        primeroX = self.Matriz.obtenerCabeceraX(valX)
        # --------------SI NO HAY NUNGUNO---------------
        if self.tam == 0:
            primeroY.siguiente = nuevo
            nuevo.anterior = primeroY
            #
            primeroX.abajo = nuevo
            nuevo.arriba = primeroX
            self.tam += 1
        else:
            # -------------------------RECORRIDO EN Y---------------------------------
            actualY = primeroY
            while actualY is not None:
                # LOS VALORES DE auxY SON EL TIPO DE OPCIÓN QUE SE ENCUENTRA EN LA
                # IMAGEN S1.png
                if valX < actualY.Casilla.posX and actualY.anterior is primeroY:
                    # auxY = 1
                    primeroY.siguiente = nuevo
                    nuevo.anterior = primeroY
                    nuevo.siguiente = actualY
                    actualY.anterior = nuevo
                    return
                elif valX < actualY.Casilla.posX and actualY.anterior is not primeroY:
                    # auxY = 2
                    if valX > actualY.anterior.Casilla.posX:
                        auxAnterior = actualY.anterior
                        auxAnterior.siguiente = nuevo
                        nuevo.anterior = auxAnterior
                        nuevo.siguiente = actualY
                        actualY.anterior = nuevo
                        return
                elif valX > actualY.Casilla.posX and actualY.siguiente is None:
                    # auxY = 3
                    actualY.siguiente = nuevo
                    nuevo.anterior = actualY
                    return
                elif actualY.siguiente is None:
                    # auxY = 4
                    primeroY.siguiente = nuevo
                    nuevo.anterior = primeroY
                    return
                actualY = actualY.siguiente
                # -------------------------RECORRIDO EN X---------------------------------
                actualX = primeroX
                while actualX is not None:
                    # LOS VALORES DE auxY SON EL TIPO DE OPCIÓN QUE SE ENCUENTRA EN LA
                    # IMAGEN S2.png
                    if valY < actualX.Casilla.posY and actualX.arriba is primeroX:
                        # auxY = 1
                        primeroX.abajo = nuevo
                        nuevo.arriba = primeroX
                        nuevo.abajo = actualX
                        actualX.arriba = nuevo
                        self.tam += 1
                        return
                    elif valY < actualX.Casilla.posY and actualX.arriba is not primeroX:
                        # auxY = 2
                        if valY > actualX.anterior.Casilla.posY:
                            auxAnterior = actualX.arriba
                            auxAnterior.abajo = nuevo
                            nuevo.arriba = auxAnterior
                            nuevo.abajo = actualX
                            actualX.arriba = nuevo
                            self.tam += 1
                            return
                    elif valY > actualX.Casilla.posY and actualX.abajo is None:
                        # auxY = 3
                        actualX.abajo = nuevo
                        nuevo.arriba = actualX
                        self.tam += 1
                        return
                    elif actualX.abajo is None:
                        # auxY = 4
                        primeroX.abajo = nuevo
                        nuevo.arriba = primeroX
                        self.tam += 1
                        return
                    actualX = actualX.abajo

            # -------------------------INSERCCION EN (Y,X)----------------------------

    def imprimirMatriz(self):
        actualY = self.primero_Y
        actualX = self.primero_X
        while actualY is not None:
            while actualX is not None:
                print(actualX.Casilla.valor)
                actualX = actualX.siguiente
            actualY = actualY.abajo
