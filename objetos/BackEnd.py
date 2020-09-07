from objetos.Casillero import Casillero

def asignarTipo(i,j,tab):
	if((i,j)in tab['posDobleLetra']):
		return 'DL'
	elif((i,j)in tab['posTripleLetra']):
		return 'TL'
	elif((i,j)in tab['posDoblePalabra']):
		return 'DP'
	elif((i,j)in tab['posTriplePalabra']):
		return 'TP'
	elif((i,j)in tab['posMenosUno']):
		return 'P1'
	elif((i,j)in tab['posMenosDos']):
		return 'P2'
	elif((i,j)in tab['posMenosTres']):
		return 'P3'			
	elif((i,j)in tab['posInicial']):
		return 'IN'
	else:
		return 'N'

class BackEnd():
		
	def __init__(self,tab):
		'''A partir de la clase Casillero, se genera una matriz ixj que representa al
		   tablero del juego''' 
		self.__backEnd=[[Casillero(j,i,asignarTipo(j,i,tab)) for i in range(15)] for j in range(15)]
		self.__disponibles=[(j,i) for i in range(15) for j in range(15)]
		
	def actualizarCasilla(self,i,j,ficha):
		'''Una vez que es puesta la ficha, se actualizan el casillero'''
		self.__backEnd[i][j].setLetra(ficha.getLetra())
		self.__backEnd[i][j].setValor(ficha.getValor())
		self.__backEnd[i][j].setImagen(ficha.getImage())
		self.__disponibles.remove((i,j))

	def getCasilla(self,i,j):
		'''Devuelve la Casilla ubicada en la posicion (i,j)'''
		return self.__backEnd[i][j]
		
	def getImagen(self,i,j):
		'''Devuelve la imagenAct de la Casilla ubicada en (i,j)'''
		return self.__backEnd[i][j].getImagen()	
		
	def getValor(self,i,j):
		return self.__backEnd[i][j].getValor()
		
	def getLetra(self,i,j):
		return self.__backEnd[i][j].getLetra()			

	def restaurarCasillero(self,i,j):
		'''La ficha es retirada del casillero y los valores de los atributos se restauran'''
		self.__backEnd[i][j].setLetra('')
		self.__backEnd[i][j].setValor(0)
		self.__backEnd[i][j].restoreImagen()
		self.__disponibles.append((i,j))
		
	def getDisponibles(self):
		return 	self.__disponibles
			
			
							
		
