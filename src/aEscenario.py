#Agente escenario
from os import system


class cEscenario:

    def __init__(self):
        self.__aFila = 0
        self.__aColumna = 0
        self.__aEscenario = []

    def sFilCol(self):
        return self.__aFila, self.__aColumna

    def sElemento(self, pFila, pColumna):
        return self.__aEscenario[pFila][pColumna]

    def mFilCol(self, d, f, c):
        self.__aEscenario[f][c] = d

    def cargarEscenario(self, pMapa):
        f = open(pMapa, 'r')
        fila = 0
        columna = 0
        while True:
            linea = f.readline()
            aux = len(linea)
            if not linea:
                break
            lista = []
            for i in range(aux):
                lista.append(linea[i])
            self.__aEscenario.append(lista)
            if columna < aux:
                columna = aux
            fila = fila + 1
        f.close()
        self.__aFila = fila
        self.__aColumna = columna - 1

    def imprimirEscenario(self):
        escena = ''
        for i in range(self.__aFila):
            aux = ''
            for j in range(self.__aColumna):
                aux = aux + self.__aEscenario[i][j]
            escena = escena + '\n' + aux
        system('cls')
        print(escena)

    def puedeAvanzar(self, d, f, c):
        avanzar = False
        if d == 'A':
            avanzar = (' ' == self.__aEscenario[f - 1][c])
        elif d == 'V':
            avanzar = (' ' == self.__aEscenario[f + 1][c])
        elif d == '<':
            avanzar = (' ' == self.__aEscenario[f][c - 1])
        else:
            avanzar = (' ' == self.__aEscenario[f][c + 1])
        return avanzar
    
    def puedeRetroceder(self, d, f, c):
        retroceder = False
        if d == 'A':
            retroceder = (' ' == self.__aEscenario[f + 1][c])
        elif d == 'V':
            retroceder = (' ' == self.__aEscenario[f - 1][c])
        elif d == '<':
            retroceder = (' ' == self.__aEscenario[f][c + 1])
        else:
            retroceder = (' ' == self.__aEscenario[f][c - 1])
        return retroceder        
        
    def puedeVoltear(self, d, f, c):
        voltear = False
        if d == 'A' or d == 'V':
            voltear = (' ' == self.__aEscenario[f][c - 1])
            if not voltear:
                voltear = (' ' == self.__aEscenario[f][c + 1])
        else:
            voltear = (' ' == self.__aEscenario[f - 1][c])
            if not voltear:
                voltear = (' ' == self.__aEscenario[f + 1][c])
        return voltear

    def coordenadas(self, f, c):
        ar = self.__aEscenario[f - 1][c]
        ab = self.__aEscenario[f + 1][c]
        iz = self.__aEscenario[f][c - 1]
        de = self.__aEscenario[f][c + 1]
        return ar, ab, iz, de
    
    def obstaculos(self, fil, col, filObjetivo, colObjetivo, direc):
        muro = self.__aEscenario[0][0]
        if (fil == filObjetivo):#si el objetivo esta en la misma fila
            if (direc=='<' and colObjetivo < col):
                if [ a for a in self.__aEscenario[fil][colObjetivo:col] if a == muro] == []:
                    return True
            if (direc=='>' and colObjetivo > col):
                if [ a for a in self.__aEscenario[fil][col:colObjetivo] if a == muro] == []:
                    return True
        if (col == colObjetivo):
            if (direc=='A' and filObjetivo < fil):
                if [ self.__aEscenario[a][col] for a in range(filObjetivo,fil) if self.__aEscenario[a][col] == muro] == []:
                    return True
            if (direc=='V' and filObjetivo > fil):
                if [ self.__aEscenario[a][col] for a in range(fil,filObjetivo) if self.__aEscenario[a][col] == muro] == []:
                    return True
        return False