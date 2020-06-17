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
unknown='./letras/NN.png' #Casillas ocultas del atril de la CPU.

cantX=cantY=15
cantFichas=7

letras=['A','B','C','D','E','F','G','H','I','J','K','L','LL','M','N','O','P','Q','R','RR','S','T','U','V','W','X','Y','Z']

#---------Posicion de los casilleros especiales---------#

posDobleLetra=[(2,2),(4,4),(6,6),(2,12),(4,10),(6,8),(8,6),(10,4),(12,2),(8,8),(10,10),(12,12),(12,6),(12,8)]
posTripleLetra=[(1,1),(3,3),(5,5),(5,9),(3,11),(1,13),(9,5),(11,3),(13,1),(9,9),(11,11),(13,13),(3,5),(1,7),(3,9)]
posDoblePalabra=[(5,3),(7,1),(9,3),(5,11),(7,13),(9,11),(11,5),(11,9),(13,7),(0,0),(14,14)]
posTriplePalabra=[(6,2),(8,2),(6,12),(8,12),(2,6),(2,8),(14,0),(0,14)]
posInicial=[(7,7)]

#-------------------------------------#

bolsa=Bolsa()
bolsa.inicializar_Bolsa()
fichas=bolsa.getFichas()

tabla=BackEnd()

#---------Tablero---------#

claves=['DL','TL','DP','TP','N']

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

def asignarClave(i,j):
	if((i,j)in posDobleLetra):
		return claves[0]
	elif((i,j)in posTripleLetra):
		return claves[1]
	elif((i,j)in posDoblePalabra):
		return claves[2]
	elif((i,j)in posTriplePalabra):
		return claves[3]
	else:
		return claves[4]
		
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

atrilCPU=[sg.Button(image_filename=unknown, image_size=(30,30),pad=(0,0)) for i in range(cantFichas)]

#---------Atril Jugador---------#

atrilJugador=[sg.Button(image_filename=fichas[i].getImage(), image_size=(30,30),key=(fichas[i].getLetra(),fichas[i].getValor(),i), pad=(0,0)) for i in range(cantFichas)]

#---------Ventana---------#
Interfaz=[[sg.Text('Atril CPU ')],
		atrilCPU,
           [sg.Column(tablero)],
           [sg.Text('Atril Jugador ')],
		atrilJugador
      ]
window = sg.Window('Scrabble').Layout(Interfaz)
while True:
	try:
		event,values=window.Read()
		if(event[0] in range(15)):
			if((tabla.comprobarCasilla(event[0],event[1]))==True)and(aux!=None): #Compruebo si la casilla esta disponible y si aux esta inicializado
				window[event].update(image_filename=aux.getImage()) #Actualizo la imagen de la casilla
				tabla.actualizarCasilla(event[0],event[1],aux.getLetra(),aux.getValor()) #Actualizo los valores del BackEnd del tablero
				window[clave].update(visible=False)  #Borro la ficha del atril
				aux=None #Reseteo aux
		elif(event[0] in letras):
			aux=Ficha(event[0]) #Si se clickeo una ficha del atril, inicializo el objeto con su letra correspondiente
			clave=event	#Guardo la clave de la ficha
	except(NameError):
		#Si el jugador hace click en el tablero antes de seleccionar una ficha, el programa no se cierra.
		pass		

window.Close()
