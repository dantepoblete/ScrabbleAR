import PySimpleGUI as sg
from Bolsa import Bolsa
from Ficha import Ficha
from BackEnd import BackEnd

#---------Ubicacion de las imagenes---------#

inicio='./img/IN.png'
normal='./img/N.png' #Casilla normal del tablero.
dobleLetra='./img/DL.png'
tripleLetra='./img/TL.png'
doblePalabra='./img/DP.png'
triplePalabra='./img/TP.png'

cantX=cantY=15

letras=['A','B','C','D','E','F','G','H','I','J','K','L','LL','M','N','O','P','Q','R','RR','S','T','U','V','W','X','Y','Z']

#---------Posicion de los casilleros especiales---------#

posDobleLetra=[(2,2),(4,4),(6,6),(2,12),(4,10),(6,8),(8,6),(10,4),(12,2),(8,8),(10,10),(12,12),(12,6),(12,8)]
posTripleLetra=[(1,1),(3,3),(5,5),(5,9),(3,11),(1,13),(9,5),(11,3),(13,1),(9,9),(11,11),(13,13),(3,5),(1,7),(3,9)]
posDoblePalabra=[(5,3),(7,1),(9,3),(5,11),(7,13),(9,11),(11,5),(11,9),(13,7),(0,0),(14,14)]
posTriplePalabra=[(6,2),(8,2),(6,12),(8,12),(2,6),(2,8),(14,0),(0,14)]
posInicial=[(7,7)]

#-------------------------------------#



tabla=BackEnd()

#---------Tablero---------#

def asignarImagen(i,j):
	if((i,j)in posDobleLetra):
		return dobleLetra
	elif((i,j)in posTripleLetra):
		return tripleLetra
	elif((i,j)in posDoblePalabra):
		return doblePalabra
	elif((i,j)in posTriplePalabra):
		return triplePalabra		
	elif((i,j)in posInicial):
		return inicio
	else:
		return normal	
		
def agregarDescripcion(i,j):
	if((i,j)in posDobleLetra):
		return 'Duplica el valor de tu letra'
	elif((i,j)in posTripleLetra):
		return 'Triplica el valor de tu letra'
	elif((i,j)in posDoblePalabra):
		return 'Duplica el valor de tu palabra'
	elif((i,j)in posTriplePalabra):
		return 'Triplca el valor de tu palabra'
	elif((i,j)in posInicial):
		return 'Coloca una ficha aqui para comenzar el juego'
	else:	
		return None	
													

tablero=[[sg.Button(tooltip=agregarDescripcion(i,j), image_filename=asignarImagen(i,j), key=(i,j), image_size=(30,30), pad=(0,0)) for j in range(cantX)] for i in range(cantY)]
	
#---------Atril CPU---------#	
atrilCPU=Atril()

#---------Atril Jugador---------#
atrilJugador=Atril()

#---------Ventana---------#
Interfaz=[[sg.Text('Atril CPU ')],
	  atrilCPU.get_atril_Cpu((),
          [sg.Column(tablero)],
          [sg.Text('Atril Jugador ')],
	  atrilJugador.get_atril_Jugador()
         ]

window = sg.Window('Scrabble').Layout(Interfaz)
while True:
	try:
		event,values=window.Read()
		if(event[0] in range(15)):
			if((tabla.comprobarCasilla(event[0],event[1]))==True)and(clave!=None):
				tabla.actualizarCasilla(event[0],event[1],clave[0],clave[1])
				window[event].update(image_filename=tabla.getImagenAct(event[0],event[1])) #Actualizo la imagen de la casilla
				window[clave].update(visible=False)  #Borro la ficha del atril
				clave=None #Reseteo aux
		elif(event[0] in letras):
			clave=event	#Guardo la clave de la ficha
	except(NameError):
		#Si el jugador hace click en el tablero antes de seleccionar una ficha, el programa no se cierra.
		pass	
window.Close()
