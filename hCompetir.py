import threading
from time import sleep
import aTanque
import aEscenario

#esto es mi codigo
class cCompetir(threading.Thread):
    
    def __init__(self, pEscenario, pTanque, pObjetivo, destruido):
        #Cargando hilo
        threading.Thread.__init__(self)
        #Cargando el escenario
        self.__aEscenario = pEscenario
        self.__aTanque = pTanque
        self.__aObjetivo = pObjetivo
        self.__cOptimo = list()
        self.__aEstado = destruido
        pass
    #esto no entiendo
    def destruido(self):
        return self.__aEstado.value == 1
    
    def noVoltear(self, up, down, left, right):
        objFil, objCol = self.__aObjetivo.sDirFilCol()[1:]
        actFil, actCol = self.__aTanque.sDirFilCol()[1:]
        ar, ab, iz, de = up, down, left, right
        if actFil>objFil:
            ab = 'X'
        else:
            ar = 'X'
        if actCol>objCol:
            de = 'X'
        else:
            iz = 'X'
        return ar, ab, iz, de

    def targetIt(self, direc, fil, col):
        filObjetivo = self.__aObjetivo.sDirFilCol()[1]
        colObjetivo = self.__aObjetivo.sDirFilCol()[2]
        if fil == filObjetivo:
            if (direc == '>'):
                if ((col+1) == colObjetivo):
                    return True
            if (direc == '>'):
                if ((col-1)== colObjetivo):
                    return True
        if col == colObjetivo:
            if (direc == 'A'):
                if ((fil-1) == filObjetivo):
                    return True
            if (direc == 'V'):
                if ((fil+1) == filObjetivo):
                    return True
        if (self.__aEscenario.obstaculos(fil,col, filObjetivo,colObjetivo,direc)):
            return True
        return False
    
    def run(self):
        velocidad, pG = self.__aTanque.sVelocidadProbGiro()
        retroceder = False
        
        while not self.destruido():
            dT, fT, cT = self.__aTanque.sDirFilCol()
            dTn, fTn, cTn = dT, fT, cT
            ar, ab, iz, de = self.__aEscenario.coordenadas(fT, cT)
            if not retroceder:
                ar, ab, iz, de = self.noVoltear(ar, ab, iz, de)
            if self.__aTanque.probabilidadVoltear() and self.__aEscenario.puedeVoltear(dT, fT, cT):
                self.__aTanque.voltear(ar, ab, iz, de)
                retroceder = False
            elif self.__aEscenario.puedeAvanzar(dT, fT, cT) and not retroceder: #and not self.__aTanque.probabilidadVoltear():   
                dTn, fTn, cTn = self.__aTanque.avanzar()
                retroceder = False
#             elif self.__aEscenario.puedeVoltear(dT, fT, cT):
#                 self.__aTanque.voltear(ar, ab, iz, de)
#                 retroceder = False                
            elif self.__aEscenario.puedeRetroceder(dT, fT, cT):
                dTn, fTn, cTn = self.__aTanque.retroceder()
                retroceder = True
            self.__aEscenario.mFilCol(' ', fT, cT)
            self.__aEscenario.mFilCol(dTn, fTn, cTn)
            self.__aEscenario.imprimirEscenario()
            sleep(velocidad)
            if self.targetIt(dTn, fTn, cTn):
                self.__aEstado.value = 1
                sleep(10)
                
