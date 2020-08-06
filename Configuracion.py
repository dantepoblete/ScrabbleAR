import PySimpleGUI as sg

tableros = {'facil':{'posDobleLetra':[(2,2),(4,4),(6,6),(2,12),(4,10),(6,8),(8,6),(10,4),(12,2),(8,8),(10,10),(12,12),(12,6),(12,8)],
				'posTripleLetra':[(1,1),(3,3),(5,5),(5,9),(3,11),(1,13),(9,5),(11,3),(13,1),(9,9),(11,11),(13,13),(3,5),(1,7),(3,9)],
				'posDoblePalabra':[(5,3),(7,1),(9,3),(5,11),(7,13),(9,11),(11,5),(11,9),(13,7),(0,0),(14,14)],
				'posTriplePalabra':[(6,2),(8,2),(6,12),(8,12),(2,6),(2,8),(14,0),(0,14)],
				'posMenosUno':[(1,4),(4,13),(7,4),(7,10),(10,1),(13,10)],
				'posMenosDos':[(1,10),(4,1),(4,7),(10,7),(10,13),(13,4)],
				'posMenosTres':[],
				'posInicial':[(7,7)]},
		'medio':{'posDobleLetra':[(0,4),(4,7),(4,14),(5,4),(5,10),(9,4),(9,10),(10,0),(10,7),(14,10)],
				'posTripleLetra':[(0,10),(4,0),(4,5),(4,9),(7,3),(7,11),(10,5),(10,9),(10,14),(14,4)],
				'posDoblePalabra':[(0,0),(2,4),(2,10),(12,4),(12,10),(14,14)],
				'posTriplePalabra':[(0,14),(4,2),(4,12),(10,2),(10,12),(14,0)],
				'posMenosUno':[(1,1),(1,13),(5,7),(7,5),(7,9),(9,7),(13,1),(13,13)],
				'posMenosDos':[(0,7),(3,3),(3,11),(11,3),(11,11),(14,7)],
				'posMenosTres':[(2,7),(7,1),(7,13),(12,7)],
				'posInicial':[(7,7)]},
		'dificil':{'posDobleLetra':[(0,14),(14,0)],
				'posTripleLetra':[(1,13),(13,1)],
				'posDoblePalabra':[(0,0),(14,14)],
				'posTriplePalabra':[(1,1),(13,13)],
				'posMenosUno':[(0,4),(2,2),(2,6),(2,8),(2,12),(4,4),(4,10),(6,2),(6,12),(8,2),(8,12),(10,0),(10,4),(10,10),(10,14),(12,2),(12,6),(12,8),(12,12),(14,4),(14,10)],
				'posMenosDos':[(0,10),(3,3),(3,11),(4,0),(4,6),(4,8),(4,14),(6,4),(6,10),(8,4),(8,10),(10,6),(10,8),(10,4),(11,3),(11,11)],
				'posMenosTres':[(1,3),(1,5),(1,9),(1,11),(3,1),(3,7),(3,13),(5,1),(5,5),(5,9),(5,13),(7,3),(7,11),(9,1),(9,5),(9,9),(9,13),(11,1),(11,7),(11,13),(13,3),(13,5),(13,9),(13,11)],
				'posInicial':[(7,7)]}
		}
fichasDefault = {'A':[1,11],'B':[3,3],'C':[2,4],'D':[2,4],'E':[1,11],'F':[4,2],'G':[2,2],'H':[4,2],'I':[1,6],'J':[6,2],'K':[8,1],
					   'L':[1,4],'LL':[8,1],'M':[3,3],'N':[1,5],'Ñ':[8,1],'O':[1,8],'P':[3,2],'Q':[8,1],'R':[1,4],'RR':[8,1],'S':[1,7],
					   'T':[1,4],'U':[1,6],'V':[4,2],'W':[8,1],'X':[8,1],'Y':[4,1],'Z':[10,1]}

ranking={'facil' : ("TopFacil.json"),'medio':("TopMedio.json"),'dificil':("TopDificil.json"),'general':("TopNiveles.json")}
			 
class Config():
	'''Esta clase contiene los tres campos configurables con valores predeterminados los cuales son:
	-Dificultad: Esta establecido con el tablero en dificultad medio.
	-Fichas: Es un diccionario con la estructura 'Letra':[Valor,Cantidad].
	-Tiempo de la partida: Esta establecido a 8 minutos de juego.'''
	def __init__(self):
		self.__nivel='medio'
		self.__tablero=tableros[self.__nivel]
		self.__fichas=fichasDefault
		self.__tiempoPartida=8*6000
		self.__topGeneral= ranking['general']
		self.__topNivel= ranking[self.__nivel]
	
	def getNivel(self):
		return self.__nivel
		
	def setNivel(self,nivel):
		self.__nivel=nivel
		
	def getTablero(self):
		return self.__tablero
		
	def setTablero(self,nivel):
		self.__tablero=tableros[nivel]
		
	def getFichas(self):
		return self.__fichas
		
	def setFichas(self,letra,valor,cantidad):
		self.__fichas[letra]=[valor,cantidad]		
		
	def getTiempo(self):
		return self.__tiempoPartida
		
	def setTiempo(self,tiempo):
		self.__tiempoPartida=tiempo*6000
 
	def getTopNivel(self):
 	    return self.__topNivel
	
	def getTopNivel2(self,nivel):
		return ranking[self.__nivel]
	
	def setTopNivel(self,nivel):
		self.__topNivel=ranking[nivel]
  
	def getTopGeneral(self):
		return self.__topGeneral
		
	def setDefaults(self):
		'''Reestablece los valores por defecto del objeto'''
		self.__nivel='medio'
		self.__tablero=tableros[self.__nivel]
		self.__tiempoPartida=8*6000
		self.__fichas=fichasDefault
		self.__topGeneral= ranking['general']
		self.__topNivel= ranking[self.__nivel]
		

background = sg.LOOK_AND_FEEL_TABLE['LightBlue']['BACKGROUND']

letras = ('A','B','C','D','E','F','G','H','I','J','K','L','LL','M','N','Ñ','O','P','Q','R','RR','S','T','U','V','W','X','Y','Z')

valores = (1,2,3,4,6,8,10)

cantidad = (1,2,3,4,5,6,7,8,9,10,11)

def main(configuracion):
	niveles = [[sg.Button('Facil',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='EASY'),
				sg.Button('Medio',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='MID'),
				sg.Button('Dificil',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='HARD')
			  ]]

	selectLetras = [[sg.Text('Letra')],[sg.Spin(values=letras, size=(3,1),initial_value=letras[0], key='LET')]]
	selectValores = [[sg.Text('Valor')],[sg.Spin(values=valores, size=(3,1),initial_value=valores[0], key='VAL')]]
	selectCantidad = [[sg.Text('Cantidad')],[sg.Spin(values=cantidad, size=(3,1),initial_value=cantidad[0], key='CANT')]]
	agregarFichas = [[sg.Button('Agregar Fichas',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='ADD')]]
	selectTiempo=[[sg.Slider(range=(1,15), orientation='h', size=(30, 20), enable_events=True, default_value=8, key='TIME')]]
	panelUno = [[sg.Column(selectLetras),sg.Column(selectValores),sg.Column(selectCantidad)],[sg.Column(agregarFichas)]]

	configUno = [[sg.Frame('Configurar Nivel',niveles)]]
	configDos = [[sg.Frame('Configurar Fichas',panelUno)]]
	configTres = [[sg.Frame('Configurar Tiempo de Juego (en minutos)',selectTiempo)]]
	
	opciones = [[sg.Button('Aceptar',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key ='OK'),
				sg.Button('Predeterminado',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key ='DEFAULT')
			  ]]
	
	layout = [[sg.Column(configUno)],[sg.Column(configDos)],[sg.Column(configTres)],[sg.Column(opciones, justification = 'center')]]

	window= sg.Window('Configuracion ScrabbleAR',layout, use_default_focus=False)
	while True:
		event,values=window.Read()
		if(event=='EASY'):
			configuracion.setNivel('facil')
			configuracion.setTablero('facil')
			configuracion.setTopNivel('facil')
		elif(event=='MID'):
			configuracion.setNivel('medio')	
			configuracion.setTablero('medio')
			configuracion.setTopNivel('medio')
		elif(event=='HARD'):
			configuracion.setNivel('dificil')
			configuracion.setTablero('dificil')
			configuracion.setTopNivel('dificil')
		elif(event=='ADD'):
			configuracion.setFichas(values['LET'],values['VAL'],values['CANT'])
			sg.popup('Se agregaron '+str(values['CANT'])+' fichas de la letra '+str(values['LET'])+' con valor de '+str(values['VAL'])+' puntos.')
		elif(event=='TIME'):
			configuracion.setTiempo(values['TIME'])
		elif(event=='OK'):
			sg.popup('La configuración fue guardada con éxito')
			break
		elif(event=='DEFAULT'):
			configuracion.setDefaults()
			sg.popup('Valores Reestablecidos')
		else:
			break	
			
	window.Close()
		
if __name__ == '__main__':
    main()
