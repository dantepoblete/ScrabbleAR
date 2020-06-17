claves=['DL','TL','DP','TP','N']

posDobleLetra=[(2,2),(4,4),(6,6),(2,12),(4,10),(6,8),(8,6),(10,4),(12,2),(8,8),(10,10),(12,12),(12,6),(12,8)]
posTripleLetra=[(1,1),(3,3),(5,5),(5,9),(3,11),(1,13),(9,5),(11,3),(13,1),(9,9),(11,11),(13,13),(3,5),(1,7),(3,9)]
posDoblePalabra=[(5,3),(7,1),(9,3),(5,11),(7,13),(9,11),(11,5),(11,9),(13,7),(0,0),(14,14)]
posTriplePalabra=[(6,2),(8,2),(6,12),(8,12),(2,6),(2,8),(14,0),(0,14)]
posInicial=[(7,7)]

def asignarTipo(i,j):
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

class BackEnd():
	def __init__(self):
		'''Crea una matriz ixj de listas, dichas listas contienen 4 datos:
		1-Tipo de casillero(DobleLetra,TripleLetra,Normal,etc.).
		2-Letra ubicada (Al estar vacio se inicializa en '').
		3-Valor de la letra ubicada (Al estar vacio se inicializa en 0).
		4-Disponibilidad del casillero(True si se puede poner una ficha y False en caso contrario,
		 al estar vacio el tablero, se inicializa en True).'''
		self.__backEnd=[[[asignarTipo(i,j),'',0,True] for i in range(15)] for j in range(15)]

	def comprobarCasilla(self,i,j):
		'''Comprueba si la casilla esta disponible y actualiza su estado'''
		if(self.__backEnd[i][j][3]==False):
			return False
		else:
			return True	

	def actualizarCasilla(self,i,j,letra,valor):
		'''Una vez que es puesta la ficha, se actualizan los valores y la disponibilidad de la casilla cambia a False'''
		self.__backEnd[i][j][1]=letra
		self.__backEnd[i][j][2]=valor
		self.__backEnd[i][j][3]=False
	
	
