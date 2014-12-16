#Aplicacion
#Cargando tanques
from aTanque import cTanque
from multiprocessing import Value
from random import randint

aT1 = cTanque(0.6, 0.9)
aT2 = cTanque(0.6, 0.9)
#Cargando el escenario
from aEscenario import cEscenario
aE = cEscenario()
aE.cargarEscenario('mapa01.txt')
#ubicando tanques
f, c = aE.sFilCol()
aT1.ubicacion(randint(0,3), 1, 4)
aT2.ubicacion(randint(0,3), f - 2, c - 2)
#Cargando hilos de competencia
from hCompetir import cCompetir
v1, pv1 = aT1.sVelocidadProbGiro()
v2, pv2 = aT2.sVelocidadProbGiro()
aT2.sVelocidadProbGiro()

destruido = Value('i',0)
hilo0 = cCompetir(aE, aT1, aT2, destruido)
hilo1 = cCompetir(aE, aT2, aT1, destruido)
hilo0.start()
hilo1.start()