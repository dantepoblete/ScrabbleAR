from Casillero import Casillero

class BackEnd():
	def __init__(self):
		'''Crea una matriz ixj de Casilleros, cada uno corresponde a un 
		casillero del tablero y contienen 4 atributos:
		1-Tipo de casillero(DobleLetra,TripleLetra,Normal,etc.).
		2-Letra ubicada (Al estar vacio se inicializa en '').
		3-Valor numerico de la letra ubicada (Al estar vacio se inicializa en 0).
		4-Disponibilidad del casillero(True si esta libre y False en caso contrario,
		 al estar vacio el tablero, se inicializa en True).'''
		self.__backEnd=[[Casillero(i,j) for i in range(15)] for j in range(15)]
		
	def getEstado(self,i,j):
		'''Devuelve el estado de la casilla ubicada en la posición [i][j]'''
		return self.__backEnd[i][j].getEstado()

	def actualizarCasilla(self,i,j,letra,valor):
		'''Una vez que es puesta la ficha, se actualizan los valores y la disponibilidad de la casilla cambia a False.'''
		self.__backEnd[i][j].setLetra(letra)
		self.__backEnd[i][j].setValor(valor)
		self.__backEnd[i][j].setEstado(False)
		self.__backEnd[i][j].setImagen(letra)

	def getCasilla(self,i,j):
		return self.__backEnd[i][j]
		
	def getImagen(self,i,j):
		return self.__backEnd[i][j].getImagen()	
		
	def getValor(self,i,j):
		return self.__backEnd[i][j].getValor()
		
	def getLetra(self,i,j):
		return self.__backEnd[i][j].getLetra()			

	def restaurarCasillero(self,i,j):
		'''La ficha es retirada del casillero'''
		self.__backEnd[i][j].setLetra('')
		self.__backEnd[i][j].setValor(0)
		self.__backEnd[i][j].setEstado(True)
		self.__backEnd[i][j].restoreImagen()
		
