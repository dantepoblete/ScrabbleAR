import PySimpleGUI as sg
from Atril import Atril
from BackEnd import BackEnd
from palabra_Valida import clasificar, palabra_Valida
from TopTen import Top
import random
import time
import os
import pickle

background = sg.LOOK_AND_FEEL_TABLE['DarkBlue2']['BACKGROUND']

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

def definirOrientacion(event,posActual):
	if(event[0] == posActual[0] + 1):
		vertical = [(event[0] + 1,event[1])]
		return vertical
	elif(event[1] == posActual[1] + 1):
		horizontal = [(event[0],event[1] + 1)]
		return horizontal
		
def resultadoFinal(totalJugador,totalCPU):
		if(totalJugador>totalCPU):
			for i in range(400000):
				sg.PopupAnimated(image_source='./img/WIN.gif',message='¡FELICIDADES, GANASTE LA PARTIDA!',time_between_frames=370)
		elif(totalJugador<totalCPU):
			for i in range(400000):
				sg.PopupAnimated(image_source='./img/LOSE.gif',message='HAS PERDIDO, MEJOR SUERTE LA PROXIMA',time_between_frames=370)
		else:
			for i in range(400000):
				sg.PopupAnimated(image_source='./img/TIE.gif',message='¡EMPATASTE, BIEN JUGADO!',time_between_frames=370)
		sg.PopupAnimated(None)
		
def main(config,carga=False):
	
	sg.change_look_and_feel('DarkBlue2')
	
	def ponerFicha(event,ficha):
		tabla.actualizarCasilla(event[0],event[1],ficha)
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
				if((i,j) not in tabla.getDisponibles()):
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
				if((i,j) not in tabla.getDisponibles()):
					ok = False
				i+=1
		return ok	
		
	def calcularPuntaje(palabra):
		total = 0
		DP = 0
		TP = 0
		descuento=0
		for letra in palabra:
			valor=letra.getValor()
			tipo=letra.getTipo()
			if(tipo =='DL'):
				valor = valor * 2
			elif(tipo =='TL'):
				valor = valor * 3
			elif(tipo =='DP'):
				DP += 1
			elif(tipo== 'TP' ):
				TP += 1
			if(tipo=='P1'):
				descuento += 1
			elif(tipo=='P2'):
				descuento += 2
			elif(tipo=='P3'):
				descuento+=3
			total += valor
		if(DP > 0):
			total = total * 2 * DP
		if(TP > 0):
			total = total * 3 *TP
		if(descuento > 0):
			total=total-descuento
		return total
		
	layout2=[[sg.Text('Ingrese el nombre de Jugador:')],
			 [sg.InputText(key='NAME', size=(30,1))],
			 [sg.Button('Aceptar',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='OK')]
			]
	ingresoNombre=sg.Window('Nueva Partida', layout2, use_default_focus=False)
		
	if(carga==True):
		guardado = './save/PartidaGuardada.pckl'
		with open(guardado,'rb')as archivo:
			recover = pickle.load(archivo)
			nivel = recover['nivel']
			mainTab = recover['mainTab']
			tabla = recover['saveTablero']
			atrilJugador = recover['saveAtrilJug']
			atrilCPU = recover['saveAtrilCPU']
			palabrasJugador = recover['palabrasJug']
			palabrasCPU = recover['palabrasCPU']
			totalJugador = recover['totalJug']
			totalCPU = recover['totalCPU']
			cambios = recover['cambios']
			tiempoActual = recover['tiempoActual']
			turno = recover['turno']
			fichasUsadas = recover['fichasUsadas']
			acertadas = recover['acertadas']
			tiempoPartida = recover['tiempoPartida']
			nombre = recover['nombre']
			topNivel= recover['rankingNivel']
			tiempoInicio=int(round(time.time()*100))-tiempoActual
	else:		
		turno=random.choice(['CPU','Jugador'])
		acertadas = 0
		fichasUsadas = 0
		nivel=config.getNivel()
		mainTab=config.getTablero()
		tabla = BackEnd(mainTab)
		cambios = 3
		tiempoPartida = config.getTiempo()
		atrilJugador = Atril(config.getFichas())
		atrilJugador.inicializarAtril()
		topNivel=Top(config.getTopNivel())
		atrilCPU = Atril(config.getFichas())
		atrilCPU.inicializarAtril()		
		palabrasJugador=[]
		palabrasCPU=[]
		totalCPU=0
		totalJugador=0
		tiempoActual = 0
		tiempoInicio = int(round(time.time()*100))
		while True:
			event,values=ingresoNombre.read()
			if(event == 'OK')and(values['NAME']!=''):
				nombre = values['NAME']
				break
			else:
				sg.popup('Ingrese un nombre para continuar')
		ingresoNombre.Close()				
	fin=False
	posSiguiente = []
	palabra = []
	posFichas =[]
	infoCambio='Le quedan '+str(cambios)+' cambios a utilizar'
	topGeneral=Top(config.getTopGeneral())
	
	espaciado = '		        '
	
	if(nivel == 'facil'):
		infoNivel= sg.Text(espaciado+'Nivel '+ nivel.upper(),text_color='LightBlue',tooltip='AYUDA: Solo puede usar adjetivos,sustantivos y verbos')
	else:
		infoNivel= sg.Text(espaciado+'Nivel ' + nivel.upper(),text_color='LightBlue', tooltip='AYUDA: Solo puede usar adjetivos y verbos')
    	
	tablero = [[sg.Button(tooltip=agregarDescripcion(i,j,mainTab), image_filename=tabla.getImagen(i,j), key=(i,j), image_size=(30,30), pad=(0,0)) for j in range(15)] for i in range(15)]
	
	CPU = [[sg.Button(image_filename='./letras/NN.png', image_size=(30,30),pad=(0,0), key=str(i)) for i in range(7)]]
	
	Jugador = [[place(sg.Button(image_filename=atrilJugador.getImagen(i), image_size=(30,30),key = int(i), pad = (0,0)))for i in range(7)]]
	
	Botones = [[sg.Button('Validar',image_filename='./img/VAL.png',image_size=(120,27),button_color=('white',background),border_width=0, pad=(0,0), key='val'),
                sg.Button('Cambiar Fichas',image_filename='./img/CF.png',image_size=(120,27),tooltip=infoCambio,button_color=('white',background),border_width=0, pad=(0,0), key='cambiar',visible=True),
                sg.Text('     Tiempo de Partida: 00:00',key='TIME')],
                [sg.Button('Ceder Turno',image_filename='./img/BT2.png',image_size=(120,27),button_color=('white',background),border_width=0,pad=(0,0), key='CED'),infoNivel]]
              
	contadorCPU = [[sg.Text(totalCPU, size=(3,1), key='TOT1')]]
	contadorJugador = [[sg.Text(totalJugador, size=(3,1), key='TOT2')]]
	venCPU = [[sg.Listbox(values=palabrasCPU, size=(20,4), key='LIS1')]]
	venJugador = [[sg.Listbox(values=palabrasJugador, size=(20,4), key='LIS2')]]
	ven2 = [[sg.Frame('Aciertos CPU',venCPU)],[sg.Frame('Puntaje CPU',contadorCPU)]]
	ven = [[sg.Frame('Aciertos de '+nombre,venJugador)],[sg.Frame('Puntaje de '+nombre,contadorJugador)]]
	Botones2 = [[sg.Button('Posponer Partida',image_filename='./img/POS.png',image_size=(120,27),button_color=('white',background),border_width=0, key='POS')],
				[sg.Button('Finalizar Partida',image_filename='./img/FIN.png',image_size=(120,27),button_color=('white',background),border_width=0, key='FIN')]
				] 
	
	logo = [[sg.Image(filename = './img/MINI.png', size = (128,76), background_color =background,key='MINI')]]
	datos= [[sg.Column(logo,justification='center')],[sg.Column(ven2)],[sg.Column(ven)],[sg.Column(Botones2)]]
	Interfaz = [[sg.Column(CPU)],[sg.Column(tablero),sg.Column(datos)],[sg.Column(Jugador),sg.Column(Botones)]]   
	
	window = sg.Window('ScrabbleAR').Layout(Interfaz)
	
	if(turno == 'CPU')and(carga==False):
		sg.popup('Empieza la CPU')
	elif(turno=='Jugador')and(carga==False):
		sg.popup('Empieza '+nombre)
	else:
		sg.popup('Continua '+nombre)	
	while True:
		if(turno == 'Jugador')and(int(round(time.time()*100))-tiempoInicio<tiempoPartida):
			event,values= window.Read(timeout=0)
			tiempoActual=int(round(time.time()*100))-tiempoInicio
			window['TIME'].update('     Tiempo de Partida: {:02d}:{:02d}'.format((tiempoActual//100)//60,(tiempoActual//100)%60))
			try:
				if(type(event) == tuple):
					if(fichasUsadas == 0)and(event[0] == 7)and(event[1] == 7)and(clave!=None):#Si es la primer ficha del juego
						posSiguiente.append((8,7))#La siguiente ficha puede ser puesta en vertical.
						posSiguiente.append((7,8))#La siguiente ficha puede ser puesta en horizontal.
						ponerFicha(event,atrilJugador.getFicha(clave))#El tablero es actualizado con la ficha puesta.
						palabra.append(tabla.getCasilla(event[0],event[1]))#La informacion del casillero es agregada a una lista para ser procesado.
						posFichas.append(clave)#Guardo la posicion de la ficha en el atril
						clave = None
						posActual = event	#La posicion actual es la de la ultima ficha ubicada(esto es asi para controlar la orientación).
						fichasUsadas = fichasUsadas + 1		#Aumento la cantidad de fichas usadas
					elif(fichasUsadas!=0)and(acertadas == 0)and(clave!=None): #Si es la segunda ficha en el juego.
						if(event in tabla.getDisponibles())and(event in posSiguiente):#Si el casillero esta disponible y su ubicacion es consecutiva a la anterior
							posSiguiente = definirOrientacion(event,posActual)
							ponerFicha(event,atrilJugador.getFicha(clave))
							palabra.append(tabla.getCasilla(event[0],event[1]))
							posFichas.append(clave)	
							clave = None
							posActual = event
							fichasUsadas = fichasUsadas + 1
					elif(acertadas != 0)and(clave!=None):
						if(event in tabla.getDisponibles())and(posSiguiente == []):
							posActual = event
							posSiguiente = [(event[0]+1,event[1]),(event[0],event[1]+1)]
							ponerFicha(event,atrilJugador.getFicha(clave))
							palabra.append(tabla.getCasilla(event[0],event[1]))
							posFichas.append(clave)	
							clave = None
							fichasUsadas = fichasUsadas + 1
						elif(event in tabla.getDisponibles())and(event in posSiguiente):
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
						word=word+letra.getLetra().lower()#Genero la palabra a partir de las fichas puestas.
						pos.append(letra.getPos())
					if(palabra_Valida(word,nivel)):
						#Completo el atril con nuevas fichas de la bolsa, en caso de no poder completar todas, las faltantes quedan en la lista noRepuestas
						noRepuestas=atrilJugador.completarAtril(posFichas)
						puntos = calcularPuntaje(palabra)
						totalJugador+=puntos
						palabrasJugador.append((word.upper(),puntos))
						window['LIS2'].update(values=palabrasJugador)
						window['TOT2'].update(totalJugador)
						for i in posFichas:
							window[i].update(image_filename=atrilJugador.getImagen(i))
							window[i].update(visible=True)
						acertadas = acertadas + 1
						if(atrilJugador.finalizarAtril()):#Si se terminaron las fichas de la bolsa del jugador
							for j in range(7):
								window[str(j)].update(image_filename=atrilCPU.getImagen(j))#Muestro las fichas del atrilCPU
							totalJugador-=atrilJugador.puntajeFinal(noRepuestas)#Al puntaje del jugador le resto el puntaje de las fichas restantes.
							totalCPU-=atrilCPU.puntajeFinal([])#Al puntaje de la IA le resto el puntaje de las fichas restantes					
							topNivel.agregarNuevoPuntaje(nombre,totalJugador,nivel.upper())#Actualizo los Tops
							topGeneral.agregarNuevoPuntaje(nombre,totalJugador,nivel.upper())
							window['TOT1'].update(totalCPU)
							window['TOT2'].update(totalJugador)
							resultadoFinal(totalJugador,totalCPU)
							break#Termino el juego
						turno='CPU'				
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
					sg.PopupQuickMessage('Seleccione las fichas a cambiar,confirme con el boton Cambiar Fichas')
					elegidas=[]
					ok=True
					while(ok == True):
						clave,values=window.read()
						if(type(clave) == int):
							if(clave in elegidas):
								sg.PopupQuickMessage('Ya se agrego')
							else:
								elegidas.append(clave)
						elif(clave=='cambiar'):
							ok=False
						elif(type(clave)!=int)and(clave!='cambiar'):
							print(type(clave))
							sg.PopupQuickMessage('Seleccione una ficha válida')	
					atrilJugador.cambiarFichas(elegidas)
					for i in elegidas:
						window[i].update(image_filename=atrilJugador.getImagen(i))
						window[i].update(visible=True)	
					cambios=cambios-1
					window['cambiar'].SetTooltip('Le quedan '+str(cambios)+' cambios a utilizar')
					if(cambios == 0): #Si el jugador se queda sin cambios de fichas
						window['cambiar'].SetTooltip('Ya no posee cambios a utilizar')
					turno='CPU'
				elif(event=='POS'):
					try:
						os.mkdir('save')
					except(FileExistsError):
						pass	
					guardado = './save/PartidaGuardada.pckl'
					#Guardo en un diccionario todas las variables escenciales del juego con sus respectivos valores al momento.
					backUp={'saveTablero':tabla,'saveAtrilJug':atrilJugador,'saveAtrilCPU':atrilCPU,
							'nivel':nivel,'mainTab':mainTab,'palabrasJug':palabrasJugador,'palabrasCPU':palabrasCPU,'totalJug':totalJugador,'totalCPU':totalCPU,
							'cambios':cambios,'tiempoPartida':tiempoPartida,'tiempoActual':tiempoActual,'turno':turno,
							'fichasUsadas':fichasUsadas,'acertadas':acertadas,'nombre':nombre,'rankingNivel': topNivel}
					with open(guardado,'wb')as archivo:
						pickle.dump(backUp,archivo)
					sg.popup('Datos Guardados')
					break
				elif(event== 'CED'):
					sg.PopupQuickMessage('Pasaste de turno')	
					turno='CPU'
				elif(event=='FIN'):
					for j in range(7):
						window[str(j)].update(image_filename=atrilCPU.getImagen(j))
					totalJugador-=atrilJugador.puntajeFinal([])
					totalCPU-=atrilCPU.puntajeFinal([])					
					topNivel.agregarNuevoPuntaje(nombre,totalJugador,nivel.upper())
					topGeneral.agregarNuevoPuntaje(nombre,totalJugador,nivel.upper())
					window['TOT1'].update(totalCPU)
					window['TOT2'].update(totalJugador)
					resultadoFinal(totalJugador,totalCPU)
					break
			except(NameError):
				pass	#Si el jugador hace click en el tablero antes de seleccionar una ficha, el programa no se cierra.
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
					combinacion.append(pos)#Agrego la posicion de la ficha seleccionada a la lista de combinacion
				palabras.append(combinacion)#Una vez generada la combinacion de fichas, la agrego a la lista de palabras generadas
			i=0
			while(i<=len(palabras)-1)and(valida==None):
				word=''
				for pos in palabras[i]:
					word+=atrilCPU.getLetra(pos).lower()
				if(palabra_Valida(word,nivel)):
					valida=palabras[i]
				else:
					i+=1
			if(valida==None):
				sg.PopupQuickMessage('El oponente pasa de turno')#Si ninguna combinacion genero una palabra valida, paso de turno
				turno='Jugador'
			else:
				if(acertadas==0):#Si el primer turno del juego corresponde a la CPU o aun no hay fichas colocadas en el tablero
					orientacion = random.choice(['Horizontal','Vertical'])#Elijo la orientacion de la palabra a poner en el atril
					pos=(7,7)#La posicion inicial es (7,7)
					for j in valida:
						tabla.actualizarCasilla(pos[0],pos[1],atrilCPU.getFicha(j))
						window[pos].update(image_filename=tabla.getImagen(pos[0],pos[1]))
						datos.append(tabla.getCasilla(pos[0],pos[1]))
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
					for j in valida:
						tabla.actualizarCasilla(pos[0],pos[1],atrilCPU.getFicha(j))
						window[pos].update(image_filename=tabla.getImagen(pos[0],pos[1]))
						datos.append(tabla.getCasilla(pos[0],pos[1]))
						fichasUsadas+=1
						if(orientacion=='Horizontal'):
							sig=pos[1]+1
							pos=(pos[0],sig)
						elif(orientacion == 'Vertical'):
							sig=pos[0]+1
							pos=(sig,pos[1])
				noRepuestas=atrilCPU.completarAtril(valida)
				puntos = calcularPuntaje(datos)
				totalCPU+= puntos
				palabrasCPU.append((word.upper(),puntos))
				window['LIS1'].update(values=palabrasCPU)
				window['TOT1'].update(totalCPU)
				acertadas+=1
				if(atrilCPU.finalizarAtril()):
					#Muestro el atril del CPU al jugador.
					for i in range(7):
						if(i not in noRepuestas):
							window[str(i)].update(image_filename=atrilCPU.getImagen(i))
						else:
							window[str(i)].update(visible=False)
					totalJugador-=atrilJugador.puntajeFinal([])
					totalCPU-=atrilCPU.puntajeFinal(noRepuestas)		
					topNivel.agregarNuevoPuntaje(nombre,totalJugador,nivel.upper())
					topGeneral.agregarNuevoPuntaje(nombre,totalJugador,nivel.upper())
					window['TOT1'].update(totalCPU)
					window['TOT2'].update(totalJugador)
					resultadoFinal(totalJugador,totalCPU)		
					break
				turno='Jugador'
		elif(int(round(time.time()*100))-tiempoInicio>=tiempoPartida): #Si se termino el tiempo actualizo los rankings y muestro el resultado final
			for j in range(7):
				window[str(j)].update(image_filename=atrilCPU.getImagen(j))#Muestro las fichas del atrilCPU
			totalJugador-=atrilJugador.puntajeFinal([])#Le resto al puntaje del jugador, el puntaje de las fichas restantes del atril.
			totalCPU-=atrilCPU.puntajeFinal([])#Le resto al puntaje del CPU, el puntaje de las fichas restantes del atril.					
			topNivel.agregarNuevoPuntaje(nombre,totalJugador,nivel.upper())
			topGeneral.agregarNuevoPuntaje(nombre,totalJugador,nivel.upper())
			window['TOT1'].update(totalCPU)
			window['TOT2'].update(totalJugador)
			resultadoFinal(totalJugador,totalCPU)#Informo el resultado de la partida.
			break
	sg.popup('¡Gracias por Jugar!')
	window.Close()
if __name__ == '__main__':
    main()	
