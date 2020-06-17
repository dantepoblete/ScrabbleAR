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
		self.__ocupados=0
		
	def getEstado(self,i,j):
		'''Devuelve el estado de la casilla ubicada en la posición [i][j]'''
		return self.__backEnd[i][j].getEstado()

	def actualizarCasilla(self,i,j,letra,valor):
		'''Una vez que es puesta la ficha, se actualizan los valores y la disponibilidad de la casilla cambia a False.'''
		self.__backEnd[i][j].setLetra(letra)
		self.__backEnd[i][j].setValor(valor)
		self.__backEnd[i][j].setEstado(False)
		self.__backEnd[i][j].setImagen(letra)
		self.__ocupados=self.__ocupados+1

	def getCasillasOcupadas(self):
		'''Devuelve la cantidad de casilleros ocupados del tablero.'''
		return self.__ocupados
		
	def getImagenAct(self,i,j):
		return self.__backEnd[i][j].getImagenAct()	
		
	def getImagenAnt(self,i,j):
		return self.__backEnd[i][j].getImagenAnt()
		
	def getValor(self,i,j):
		return self.__backEnd[i][j].getValor()
		
	def getLetra(self,i,j):
		return self.__backEnd[i][j].getLetra()			

	def comprobarCasilla(self,i,j):
		'''Comprueba que la primer ficha del juego sea colocada en el casillero principal, si ya fue colocada
		solamente devuelve el estado de la casilla solicitada.'''
		if(self.getCasillasOcupadas()==0)and(i!=7)and(j!=7):
			return False
		elif(self.getCasillasOcupadas()==0)and(i==7)and(j==7):
			return True	
		elif(self.getCasillasOcupadas()!=0):
		    return self.getEstado(i,j)
