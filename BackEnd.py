from Casillero import Casillero

class BackEnd():
	def __init__(self):
		'''A partir de la clase Casillero, se genera una matriz ixj que representa al
		   tablero del juego'''
		self.__backEnd=[[Casillero(j,i) for i in range(15)] for j in range(15)]
		
	def getEstado(self,i,j):
		'''Devuelve el estado de la casilla ubicada en la posición [i][j]'''
		return self.__backEnd[i][j].getEstado()

	def actualizarCasilla(self,i,j,letra,valor):
		'''Una vez que es puesta la ficha, se actualizan el casillero'''
		self.__backEnd[i][j].setLetra(letra)
		self.__backEnd[i][j].setValor(valor)
		self.__backEnd[i][j].setEstado(False)
		self.__backEnd[i][j].setImagen(letra)

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
		self.__backEnd[i][j].setEstado(True)
		self.__backEnd[i][j].restoreImagen()
		
