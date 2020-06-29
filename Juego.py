import PySimpleGUI as sg
from Atril import Atril
from BackEnd import BackEnd
from palabra_Valida import clasificar, palabra_Valida
import random

background = sg.LOOK_AND_FEEL_TABLE['DarkBlue2']['BACKGROUND']

#---------Ubicacion de las imagenes---------#

inicio='./img/IN.png'
normal='./img/N.png' #Casilla normal del tablero.
dobleLetra='./img/DL.png'
tripleLetra='./img/TL.png'
doblePalabra='./img/DP.png'
triplePalabra='./img/TP.png'
unknown='./letras/NN.png' #Casillas ocultas del atril de la CPU.

#---------Posicion de los casilleros especiales---------#

posDobleLetra=[(2,2),(4,4),(6,6),(2,12),(4,10),(6,8),(8,6),(10,4),(12,2),(8,8),(10,10),(12,12),(12,6),(12,8)]
posTripleLetra=[(1,1),(3,3),(5,5),(5,9),(3,11),(1,13),(9,5),(11,3),(13,1),(9,9),(11,11),(13,13),(3,5),(1,7),(3,9)]
posDoblePalabra=[(5,3),(7,1),(9,3),(5,11),(7,13),(9,11),(11,5),(11,9),(13,7),(0,0),(14,14)]
posTriplePalabra=[(6,2),(8,2),(6,12),(8,12),(2,6),(2,8),(14,0),(0,14)]
posInicial=[(7,7)]

#-------------------------------------#

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
    return sg.Column([[elem]], pad=(0,0))

def ponerFicha(event,ficha):
	tabla.actualizarCasilla(event[0],event[1],ficha.getLetra(),ficha.getValor())
	window[event].update(image_filename=tabla.getImagen(event[0],event[1]))
	window[clave].update(visible=False)
	
def definirOrientacion(event,posActual):
	if(event[0] == posActual[0] + 1):
		vertical = [(event[0] + 1,event[1])]
		return vertical
	elif(event[1] == posActual[1] + 1):
		horizontal = [(event[0],event[1] + 1)]
		return horizontal


def main():
	
	def ponerFicha(event,ficha):
		tabla.actualizarCasilla(event[0],event[1],ficha.getLetra(),ficha.getValor())
		window[event].update(image_filename=tabla.getImagen(event[0],event[1]))
		window[clave].update(visible=False)
	
	
	niveles= [[sg.Button('Facil',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-facil-'))],
          	  [sg.Button('Medio',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-medio-'))]	,
		  [sg.Button('Dificil',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-dificl-'))]
		 ] 

	Dificultad = sg.Window('Dificultades', niveles)
	sg.popup('Elige un nivel de dificultad')
	event,values= Dificultad.Read()	
	if(event == 'facil'):
		nivel='facil'
	elif (event=='medio'):
         	nivel='medio'
	else:		
		nivel='dificil'		
	Dificultad.close()
	
	turno=random.choice(['CPU','Jugador'])
	acertadas = 0
	fichasUsadas = 0
	posSiguiente = []
	palabra = []
	posFichas =[]
	tabla = BackEnd()
	atrilJugador = Atril()
	atrilJugador.inicializarAtril()
	atrilCPU = Atril()
	atrilCPU.inicializarAtril()
	
	tablero = [[sg.Button(tooltip=agregarDescripcion(i,j), image_filename=asignarImagen(i,j), key=(i,j), image_size=(30,30), pad=(0,0)) for j in range(15)] for i in range(15)]
	
	CPU = [[sg.Button(image_filename=unknown, image_size=(30,30),pad=(0,0)) for i in range(7)]]
	
	Jugador = [[place(sg.Button(image_filename=atrilJugador.getImagen(i), image_size=(30,30),key = i, pad = (0,0)))for i in range(7)]]
	
	Botones = [[sg.Button('Validar',image_filename='./img/VAL.png',image_size=(120,27),button_color=('white',background),border_width=0, key='val'),
                sg.Button('Cambiar Fichas',image_filename='./img/CF.png',image_size=(120,27),button_color=('white',background),border_width=0,key='cambiar')
              ]]
	
	Interfaz=[[sg.Column(CPU)],[sg.Column(tablero)],[sg.Column(Jugador),sg.Column(Botones)]]
	
	window = sg.Window('Scrabble').Layout(Interfaz)
	
	if(turno == 'CPU'):
		sg.popup('Empieza la CPU')
	else:
		sg.popup('Empieza el Jugador')
	
	while True:
		if(turno == 'Jugador'):
			print('Turno del Jugador')
			try:
				event,values= window.Read()
				if(type(event) == tuple):
					#Si todavia no fue puesta ninguna ficha trabajo con el casillero principal
					if(fichasUsadas == 0)and(event[0] == 7)and(event[1] == 7)and(clave!=None):
						#Guardo como posibles posiciones siguientes el casillero de abajo y el de la derecha
						posSiguiente.append((8,7))
						posSiguiente.append((7,8))
						#Actualizo el casillero con la ficha puesta
						ponerFicha(event,atrilJugador.getFicha(clave))
						#Agrego a la lista 'palabra' la informacion del casillero
						palabra.append(tabla.getCasilla(event[0],event[1]))
						posFichas.append(clave)
						clave = None
						posActual = event
						fichasUsadas = fichasUsadas + 1
					elif(fichasUsadas!=0)and(acertadas == 0)and(clave!=None):
						if(tabla.getEstado(event[0],event[1]) == True)and(event in posSiguiente):
							posSiguiente = definirOrientacion(event,posActual)
							ponerFicha(event,atrilJugador.getFicha(clave))
							palabra.append(tabla.getCasilla(event[0],event[1]))
							posFichas.append(clave)	
							clave = None
							posActual = event
							fichasUsadas = fichasUsadas + 1
					elif(acertadas != 0)and(clave!=None):
						if(tabla.getEstado(event[0],event[1]) == True)and(posSiguiente == []):
							posActual = event
							posSiguiente = [(event[0]+1,event[1]),(event[0],event[1]+1)]
							ponerFicha(event,atrilJugador.getFicha(clave))
							palabra.append(tabla.getCasilla(event[0],event[1]))
							posFichas.append(clave)	
							clave = None
							fichasUsadas = fichasUsadas + 1
						elif(tabla.getEstado(event[0],event[1]) == True)and(event in posSiguiente):
							posSiguiente = definirOrientacion(event,posActual)
							ponerFicha(event,atrilJugador.getFicha(clave))
							palabra.append(tabla.getCasilla(event[0],event[1]))
							posFichas.append(clave)	
							clave = None
							posActual = event
							fichasUsadas = fichasUsadas + 1
				elif(type(event) == int):
					clave=event	#Guardo la clave de la ficha
				elif(event == 'val'):
					word = ''
					pos = []
					for letra in palabra:
						word=word+letra.getLetra().lower()
						pos.append(letra.getPos())	
					print(word)
					if(palabra_Valida(word,nivel)):
						atrilJugador.completarAtril(posFichas)
						for i in posFichas:
							window[i].update(image_filename=atrilJugador.getImagen(i))
							window[i].update(visible=True)
						acertadas = acertadas + 1
						turno = 'CPU'				
					else:
						for i in posFichas:
							window[i].update(visible=True)
						for event in pos:
							tabla.restaurarCasillero(event[0],event[1])
							window[event].update(image_filename=tabla.getImagen(event[0],event[1]))
						fichasUsadas = fichasUsadas - len(palabra)
					posSiguiente = []
					palabra = []
					posFichas=[]
				elif(event == None,'Exit'):
					break		
			except(NameError):
			#Si el jugador hace click en el tablero antes de seleccionar una ficha, el programa no se cierra.
				pass
		elif(turno == 'CPU'):
			print('Turno del CPU')
			turno = 'Jugador'
	
	window.Close()
	
if __name__ == '__main__':
    main()				
