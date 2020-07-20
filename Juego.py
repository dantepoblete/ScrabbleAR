import PySimpleGUI as sg
from Atril import Atril
from BackEnd import BackEnd
from palabra_Valida import clasificar, palabra_Valida
import random
import time

background = sg.LOOK_AND_FEEL_TABLE['DarkBlue2']['BACKGROUND']


#---------Posicion de los casilleros especiales---------#

tableroFacil={'posDobleLetra':[(2,2),(4,4),(6,6),(2,12),(4,10),(6,8),(8,6),(10,4),(12,2),(8,8),(10,10),(12,12),(12,6),(12,8)],
			  'posTripleLetra':[(1,1),(3,3),(5,5),(5,9),(3,11),(1,13),(9,5),(11,3),(13,1),(9,9),(11,11),(13,13),(3,5),(1,7),(3,9)],
			  'posDoblePalabra':[(5,3),(7,1),(9,3),(5,11),(7,13),(9,11),(11,5),(11,9),(13,7),(0,0),(14,14)],
			  'posTriplePalabra':[(6,2),(8,2),(6,12),(8,12),(2,6),(2,8),(14,0),(0,14)],
			  'posMenosUno':[],
			  'posMenosDos':[],
			  'posMenosTres':[],
			  'posInicial':[(7,7)]
			 }
tableroMedio={'posDobleLetra':[(0,4),(4,7),(4,14),(5,4),(5,10),(9,4),(9,10),(10,0),(10,7),(14,10)],
			  'posTripleLetra':[(0,10),(4,0),(4,5),(4,9),(7,3),(7,11),(10,5),(10,9),(10,14),(14,4)],
			  'posDoblePalabra':[(0,0),(2,4),(2,10),(12,4),(12,10),(14,14)],
			  'posTriplePalabra':[(0,14),(4,2),(4,12),(10,2),(10,12),(14,0)],
			  'posMenosUno':[(1,1),(1,13),(5,7),(7,5),(7,9),(9,7),(13,1),(13,13)],
			  'posMenosDos':[(0,7),(3,3),(3,11),(11,3),(11,11),(14,7)],
			  'posMenosTres':[(2,7),(7,1),(7,13),(12,7)],
			  'posInicial':[(7,7)]
			 }		 
			 

#-------------------------------------#

def asignarImagen(i,j,tab):
	if((i,j)in tab['posDobleLetra']):
		return './img/DL.png'
	elif((i,j)in tab['posTripleLetra']):
		return './img/TL.png'
	elif((i,j)in tab['posDoblePalabra']):
		return './img/DP.png'
	elif((i,j)in tab['posTriplePalabra']):
		return './img/TP.png'
	elif((i,j)in tab['posMenosUno']):
		return './img/P1.png'
	elif((i,j)in tab['posMenosDos']):
		return './img/P2.png'
	elif((i,j)in tab['posMenosTres']):
		return './img/P3.png'					
	elif((i,j) in tab['posInicial']):
		return './img/IN.png'
	else:
		return './img/N.png'	

def agregarDescripcion(i,j,tab):
	if((i,j)in tab['posDobleLetra']):
		return 'Duplica el valor de tu letra'
	elif((i,j)in tab['posTripleLetra']):
		return 'Triplica el valor de tu letra'
	elif((i,j)in tab['posDoblePalabra']):
		return 'Duplica el valor de tu palabra'
	elif((i,j)in tab['posTriplePalabra']):
		return 'Triplca el valor de tu palabra'
	elif((i,j)in tab['posMenosUno']):
		return 'Resta 1 punto a tu palabra'
	elif((i,j)in tab['posMenosDos']):
		return 'Resta 2 puntos a tu palabra'
	elif((i,j)in tab['posMenosTres']):
		return 'Resta 3 puntos a tu palabra'					
	elif((i,j) in tab['posInicial']):
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
		
	def horizontal(pos,palabra):
		ok = True
		i = pos[0]
		j = pos[1]
		if(j+len(palabra)>14):
			ok = False
		else:	
			for letra in palabra:
				if(tabla.getEstado(i,j) == False):
					ok = False
				j+=1
		return ok	
		
	def vertical(pos,palabra):
		ok = True
		i = pos[0]
		j = pos[1]
		if(i+len(palabra)>14):
			ok = False
		else:	
			for letra in palabra:
				if(tabla.getEstado(i,j) == False):
					ok = False
				i+=1
		return ok	
		
	def calcularPuntaje(palabra):
		total = 0
		DP = False
		TP = False
		for letra in palabra:
			valor=letra.getValor()
			tipo=letra.getTipo()
			print(tipo)
			if(tipo == 'DL'):
				valor = valor * 2
			elif(tipo == 'TL'):
				valor = valor * 3		
			elif(tipo == 'DP'):
				DP = True
			elif(tipo == 'TP'):
				TP = True
			total = total + valor
		if(DP == True):
			total = total * 2
		if(TP == True):
			total = total * 3
		return total
		
	niveles = [[sg.Button('Facil',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('facil'))],
          	  [sg.Button('Medio',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('medio'))]	,
			  [sg.Button('Dificil',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('dificil'))]
			  ] 

	Dificultad = sg.Window('Dificultades', niveles,use_default_focus=False)
	sg.popup('Elige un nivel de dificultad')
	event,values= Dificultad.Read()	
	if(event == 'facil'):
	 	 nivel='facil'
	 	 tab=tableroFacil
	 	 cambios=4
	 	 tiempoPartida=12000#2 minutos
	elif (event=='medio'):
         nivel='medio'
         tab=tableroMedio
         cambios=3
         tiempoPartida=18000#3 minutos
	else:		
		 nivel='dificil'
		 tab=tableroMedio
		 cambios=2
		 tiempoPartida=24000#4 minutos
	Dificultad.close()
	
	turno=random.choice(['CPU','Jugador'])
	
	acertadas = 0
	fichasUsadas = 0
	posSiguiente = []
	palabra = []
	posFichas =[]
	tabla = BackEnd(tab)
	atrilJugador = Atril()
	atrilJugador.inicializarAtril()
	atrilCPU = Atril()
	atrilCPU.inicializarAtril()
	palabrasJugador=[]
	palabrasCPU=[]
	totalCPU=0
	totalJugador=0
	tiempoActual = 0
	tiempoInicio = int(round(time.time()*100))
	fin=False
		
	infoCambio='Le quedan '+str(cambios)+' cambios a utilizar'	
    	
	tablero = [[sg.Button(tooltip=agregarDescripcion(i,j,tab), image_filename=asignarImagen(i,j,tab), key=(i,j), image_size=(30,30), pad=(0,0)) for j in range(15)] for i in range(15)]
	
	CPU = [[sg.Button(image_filename='./letras/NN.png', image_size=(30,30),pad=(0,0), key='?') for i in range(7)]]
	
	Jugador = [[place(sg.Button(image_filename=atrilJugador.getImagen(i), image_size=(30,30),key = int(i), pad = (0,0)))for i in range(7)]]
	
	Botones = [[sg.Button('Validar',image_filename='./img/VAL.png',image_size=(120,27),button_color=('white',background),border_width=0, pad=(0,0), key='val'),
                sg.Button('Cambiar Fichas',image_filename='./img/CF.png',image_size=(120,27),tooltip=infoCambio,button_color=('white',background),border_width=0, pad=(0,0), key='cambiar',visible=True),
                sg.Text('     Tiempo de Partida: 00:00',key='TIME')
                ]]
              
	contadorCPU = [[sg.Text(totalCPU, size=(3,1), key='TOT1')]]
	contadorJugador = [[sg.Text(totalJugador, size=(3,1), key='TOT2')]]
	venCPU = [[sg.Listbox(values=palabrasCPU, size=(20,4), key='LIS1')]]
	venJugador = [[sg.Listbox(values=palabrasJugador, size=(20,4), key='LIS2')]]
	ven2 = [[sg.Frame('Palabras Acertadas CPU',venCPU)],[sg.Frame('Total Puntos CPU',contadorCPU)]]
	ven = [[sg.Frame('Palabras Acertadas Jugador',venJugador)],[sg.Frame('Total Puntos Jugador',contadorJugador)]]
	Botones2 = [[sg.Button('Posponer Partida',image_filename='./img/POS.png',image_size=(120,27),button_color=('white',background),border_width=0, key='POS')],
				[sg.Button('Finalizar Partida',image_filename='./img/FIN.png',image_size=(120,27),button_color=('white',background),border_width=0, key='FIN')]
				]
	logo = [[sg.Image(filename = './img/MINI.png', size = (128,76), background_color =background,key='MINI')]]
	
	datos= [[sg.Column(logo,justification='center')],[sg.Column(ven2)],[sg.Column(ven)],[sg.Column(Botones2)]]
	Interfaz = [[sg.Column(CPU)],[sg.Column(tablero),sg.Column(datos)],[sg.Column(Jugador),sg.Column(Botones)]]     
	
	window = sg.Window('ScrabbleAR').Layout(Interfaz)
	
	if(turno == 'CPU'):
		sg.popup('Empieza la CPU')
	else:
		sg.popup('Empieza el Jugador')
	while True and fin==False:
		if(turno == 'Jugador')and(int(round(time.time()*100))-tiempoInicio<tiempoPartida):
			event,values= window.Read(timeout=0)
			tiempoActual=int(round(time.time()*100))-tiempoInicio
			window['TIME'].update('     Tiempo de Partida: {:02d}:{:02d}'.format((tiempoActual // 100) // 60,(tiempoActual // 100) % 60))
			try:
				if(type(event) == tuple):
					if(fichasUsadas == 0)and(event[0] == 7)and(event[1] == 7)and(clave!=None):
						posSiguiente.append((8,7))
						posSiguiente.append((7,8))
						ponerFicha(event,atrilJugador.getFicha(clave))
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
					if(palabra_Valida(word,nivel)):
						atrilJugador.completarAtril(posFichas)
						puntos = calcularPuntaje(palabra)
						totalJugador+=puntos
						palabrasJugador.append((word.upper(),puntos))
						window['LIS2'].update(values=palabrasJugador)
						window['TOT2'].update(totalJugador)
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
				elif(event =='cambiar')and(cambios>0):
					sg.popup('Seleccione las fichas a cambiar,confirme con el boton Cambiar Fichas')
					elegidas=[]
					ok=True
					while(ok == True):
						clave,values=window.read()
						if(type(clave) == int):
							if(clave in elegidas):
								sg.popup('Ya se agrego')
							else:
								elegidas.append(clave)
						elif(clave=='cambiar'):
							ok=False
						elif(type(clave)!=int)and(clave!='cambiar'):
							print(type(clave))
							sg.popup('Seleccione una ficha válida')	
					atrilJugador.cambiarFichas(elegidas)
					for i in elegidas:
						window[i].update(image_filename=atrilJugador.getImagen(i))
						window[i].update(visible=True)	
					cambios=cambios-1
					window['cambiar'].SetTooltip('Le quedan '+str(cambios)+' cambios a utilizar')
					if(cambios == 0): #Si el jugador se queda sin cambios de fichas
						window['cambiar'].SetTooltip('Ya no posee cambios a utilizar')
					turno='CPU'
				elif(event=='FIN'):
					sg.popup_no_wait('¿Desea salir del juego?')
			except(NameError):
			#Si el jugador hace click en el tablero antes de seleccionar una ficha, el programa no se cierra.
				pass
		elif(turno == 'CPU')and(int(round(time.time()*100))-tiempoInicio<tiempoPartida):
			window.Finalize()
			tiempoActual=int(round(time.time()*100))-tiempoInicio
			window['TIME'].update('     Tiempo de Partida: {:02d}:{:02d}'.format((tiempoActual // 100) // 60,(tiempoActual // 100) % 60))
			palabras=[]
			datos=[]
			valida=None
			cant=random.randint(2,7)#La palabra valida debe ser minimo de dos letras por lo que para cada turno genero una longitud de palabra fija de entre 2 y 7 letras
			for i in range(100):#Por cada turno genero 100 posibles combinaciones con las fichas disponibles
				fichas=[0,1,2,3,4,5,6]#Utilizo una lista con las posiciones de las fichas del atril para controlar su uso
				combinacion=[]#Inicializo una lista que guarde la combinacion generada de las fichas en cada iteracion de las 100
				for j in range(cant):#Itero tantas veces como letras deba tener la palabra
					pos=random.choice(fichas)#Elijo una ficha al azar del atril
					fichas.remove(pos)#Elimino la posibilidad de elegir la misma ficha en la proxima iteracion.
					combinacion.append(atrilCPU.getFicha(pos))#Agrego la ficha seleccionada a la lista de combinacion
				palabras.append(combinacion)#Una vez generada la combinacion de fichas, la agrego a la lista de palabras generadas
			i=0
			while(i<=len(palabras)-1)and(valida==None):
				word=''
				for ficha in palabras[i]:
					word+=ficha.getLetra().lower()
				if(palabra_Valida(word,nivel)):
					valida=palabras[i]
				else:
					i+=1
			if(valida==None):
				sg.popup('El oponente pasa de turno')#Si ninguna combinacion genero una palabra valida, paso de turno
				turno='Jugador'
			else:
				if(acertadas==0):#Si el primer turno del juego corresponde a la CPU o aun no hay fichas colocadas en el tablero
					orientacion = random.choice(['Horizontal','Vertical'])#Elijo la orientacion de la palabra a poner en el atril
					pos=(7,7)#La posicion inicial es (7,7)
					for ficha in valida:
						tabla.actualizarCasilla(pos[0],pos[1],ficha.getLetra(),ficha.getValor())
						window[pos].update(image_filename=tabla.getImagen(pos[0],pos[1]))
						datos.append(tabla.getCasilla(pos[0],pos[1]))
						atrilCPU.quitarFicha(ficha)#Quito la ficha del atril del CPU
						fichasUsadas+=1	#Aumento la cantidad de fichas utilizadas
						if(orientacion=='Horizontal'):#Si la posicion elegida fue Horizontal, la sig posicion de la ficha a colocar sera a la derecha.
							sig=pos[1]+1
							pos=(pos[0],sig)
						elif(orientacion == 'Vertical'):#Si la posicion elegida fue Vertical, la sig posicion de la ficha a colocar sera abajo.
							sig=pos[0]+1
							pos=(sig,pos[1])
				elif(acertadas!=0):
					pos=random.choice(tabla.getDisponibles())#Elijo una posicion disponible para utilizar en el tablero
					while(horizontal(pos,valida)==False)and(vertical(pos,valida)==False):	#Si la palabra generada supera los margenes del tablero desde la posicion del tablero, elijo otra
						pos=random.choice(tabla.getDisponibles())
					if(horizontal(pos,valida)==True):	#Si la palabra puede colocarse en vertical, se elige esa orientacion
						orientacion='Horizontal'
					else:	#Si la palabra puede colocarse en horizontal, se elige esa orientacion
						orientacion='Vertical'
					for ficha in valida:
						tabla.actualizarCasilla(pos[0],pos[1],ficha.getLetra(),ficha.getValor())
						window[pos].update(image_filename=tabla.getImagen(pos[0],pos[1]))
						datos.append(tabla.getCasilla(pos[0],pos[1]))
						atrilCPU.quitarFicha(ficha)
						fichasUsadas+=1
						if(orientacion=='Horizontal'):
							sig=pos[1]+1
							pos=(pos[0],sig)
						elif(orientacion == 'Vertical'):
							sig=pos[0]+1
							pos=(sig,pos[1])
				atrilCPU.completarAtrilCPU(valida)
				puntos = calcularPuntaje(datos)
				totalCPU+= puntos
				palabrasCPU.append((word.upper(),puntos))
				window['LIS1'].update(values=palabrasCPU)
				window['TOT1'].update(totalCPU)
				acertadas+=1
				turno='Jugador'
		elif(int(round(time.time()*100))-tiempoInicio>=tiempoPartida):
			window.Finalize()
			if(totalJugador>totalCPU):
				sg.popup('Ganaste')
			elif(totalJugador==totalCPU):
				sg.popup('Empate')
			else:
				sg.popup('Perdiste')
			fin=True							
	window.Close()
	
if __name__ == '__main__':
    main()				

