from random import randint
#Agente tanque


class cTanque():

    def __init__(self, pProbVoltear, pVelocidad):
        self.__aDireccion = ''
        self.__aFila = 0
        self.__aColumna = 0
        #probabilidad de giro
        self.__aProbVoltear = pProbVoltear
        self.__aVelocidad = 1 - pVelocidad

    def sDirFilCol(self):
        return self.__aDireccion, self.__aFila, self.__aColumna

    def sVelocidadProbGiro(self):
        return self.__aVelocidad, self.__aProbVoltear

    def ubicacion(self, pDireccion, pFila, pColumna):
        direccion = {0: 'A', 1: 'V', 2: '<', 3: '>'}
        self.__aDireccion = direccion[pDireccion]
        self.__aFila = pFila
        self.__aColumna = pColumna

    def avanzar(self):
        if self.__aDireccion == 'A':
            self.__aFila = self.__aFila - 1
        elif self.__aDireccion == 'V':
            self.__aFila = self.__aFila + 1
        elif self.__aDireccion == '<':
            self.__aColumna = self.__aColumna - 1
        else:
            self.__aColumna = self.__aColumna + 1
        return self.__aDireccion, self.__aFila, self.__aColumna

    def retroceder(self):
        if self.__aDireccion == 'A':
            self.__aFila = self.__aFila + 1
        elif self.__aDireccion == 'V':
            self.__aFila = self.__aFila - 1
        elif self.__aDireccion == '<':
            self.__aColumna = self.__aColumna + 1
        else:
            self.__aColumna = self.__aColumna - 1
        return self.__aDireccion, self.__aFila, self.__aColumna

    def voltear(self, ar, ab, iz, de):
        
        if self.__aDireccion == 'A' or self.__aDireccion == 'V':
            if iz == ' ' and de == ' ':
                self.__aDireccion = '<' if (randint(0, 1) == 0) else '>'
            elif iz == ' ':
                self.__aDireccion = '<'
            elif de == ' ':
                self.__aDireccion = '>'
        else:
            if ar == ' ' and ab == ' ':
                self.__aDireccion = 'A' if (randint(0, 1) == 0) else 'V'
            elif ar == ' ':
                self.__aDireccion = 'A'
            elif ab == ' ':
                self.__aDireccion = 'V'

    def probabilidadVoltear(self):
        prob = self.__aProbVoltear * 10
        giro = randint(0, 10)
        return prob > giro