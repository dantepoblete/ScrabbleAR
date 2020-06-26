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

acertadas=0
fichasUsadas=0
posSiguiente=[]
palabra=[]
palabras=['on','no','al','as','mo']

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
		
def place(elem):
	#Este es una funcion que compartio un desarrollador de PySimpleGUI, ya que al hacer window[event].update(visible=True) como en la linea 150
	#los botones aparacian pero uno encima del otro, esta funcion convierte a cada boton en una columna para respetar el orden
    return sg.Column([[elem]], pad=(0,0))

def ponerFicha(event,clave):
	tabla.actualizarCasilla(event[0],event[1],clave[0],clave[1])
	window[event].update(image_filename=tabla.getImagen(event[0],event[1]))
	window[clave].update(visible=False)
	
def definirOrientacion(event,posActual):
	if(event[0] == posActual[0] + 1):
		vertical = [(event[0] + 1,event[1])]
		return vertical
	elif(event[1] == posActual[1] + 1):
		horizontal = [(event[0],event[1] + 1)]
		return horizontal			
													

tablero=[[sg.Button(tooltip=agregarDescripcion(i,j), image_filename=asignarImagen(i,j), key=(i,j), image_size=(30,30), pad=(0,0)) for j in range(cantX)] for i in range(cantY)]
	
#---------Atril CPU---------#	

atrilCPU=[sg.Button(image_filename=unknown, image_size=(30,30),pad=(0,0)) for i in range(cantFichas)]

#---------Atril Jugador---------#

atrilJugador=[[place(sg.Button(image_filename=fichas[i].getImage(), image_size=(30,30),key=(fichas[i].getLetra(),fichas[i].getValor()), pad=(0,0)))for i in range(cantFichas)]]

#---------Ventana---------#
Interfaz=[[sg.Text('Atril CPU ')],
		atrilCPU,
           [sg.Column(tablero)],
           [sg.Text('Atril Jugador ')],
           [sg.Column(atrilJugador)],
           [sg.Button('Validar',key='val')]
      ]
window = sg.Window('Scrabble').Layout(Interfaz)
while True:
	try:
		event,values=window.Read()
		if(event[0] in range(15)):
			#Si todavia no fue puesta ninguna ficha trabajo con el casillero principal
			if(fichasUsadas == 0)and(event[0] == 7)and(event[1] == 7)and(clave!=None):
				#Guardo como posibles posiciones siguientes el casillero de abajo y el de la derecha
				posSiguiente.append((8,7))
				posSiguiente.append((7,8))
				#Actualizo el casillero con la ficha puesta
				ponerFicha(event,clave)
				#Agrego a la lista 'palabra' la informacion del casillero
				palabra.append(tabla.getCasilla(event[0],event[1]))
				clave = None
				posActual = event
				fichasUsadas = fichasUsadas + 1
			elif(fichasUsadas!=0)and(clave!=None):
				if(tabla.getEstado(event[0],event[1]) == True)and(event in posSiguiente):
					posSiguiente = definirOrientacion(event,posActual)
					ponerFicha(event,clave)
					palabra.append(tabla.getCasilla(event[0],event[1]))	
					clave = None
					posActual = event
					fichasUsadas = fichasUsadas + 1
		elif(event[0] in letras):
			clave=event	#Guardo la clave de la ficha
		elif(event == 'val'):
			word=''
			for letra in palabra:
				word=word+letra.getLetra().lower()	
			print(word)
			if(word in palabras):
				print('felicidades')
				pala
				for letra in palabra:
					#clave corresponde a la variable clave del atril
					clave=(letra.getLetra(),letra.getValor())
					#Si la palabra fue correcta por cada letra de la palabra actualizo las fichas utilizadas y las hago aparecer en el atril
					window[clave].update(image_filename=fichas[8].getImage(), image_size=(30,30),key=(fichas[8].getLetra(),fichas[8].getValor()), pad=(0,0))
					window[clave].update(visible=True)			
			else:
				#Guardo la posicion de cada casillero
				pos=[]
				for letra in palabra:
					clave=(letra.getLetra(),letra.getValor())
					window[clave].update(visible=True)
					pos.append(letra.getPos())
				for event in pos:
					tabla.restaurarCasillero(event[0],event[1])	
					window[event].update(image_filename=tabla.getImagen(event[0],event[1]))	
	except(NameError):
		#Si el jugador hace click en el tablero antes de seleccionar una ficha, el programa no se cierra.
		pass	
window.Close()
