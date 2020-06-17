posDobleLetra=[(2,2),(4,4),(6,6),(2,12),(4,10),(6,8),(8,6),(10,4),(12,2),(8,8),(10,10),(12,12),(12,6),(12,8)]
posTripleLetra=[(1,1),(3,3),(5,5),(5,9),(3,11),(1,13),(9,5),(11,3),(13,1),(9,9),(11,11),(13,13),(3,5),(1,7),(3,9)]
posDoblePalabra=[(5,3),(7,1),(9,3),(5,11),(7,13),(9,11),(11,5),(11,9),(13,7),(0,0),(14,14)]
posTriplePalabra=[(6,2),(8,2),(6,12),(8,12),(2,6),(2,8),(14,0),(0,14)]

def asignarTipo(i,j):
	if((i,j)in posDobleLetra):
		return 'DL'
	elif((i,j)in posTripleLetra):
		return 'TL'
	elif((i,j)in posDoblePalabra):
		return 'DP'
	elif((i,j)in posTriplePalabra):
		return 'TP'
	else:
		return 'N'
		
class Casillero():
	def __init__(self,i,j):
		self.__tipo=asignarTipo(i,j)
		self.__letra=''
		self.__valor=0
		self.__estado=True
		self.__imagenAnt=''
		self.__imagenAct='.img/'+self.__tipo+'.png'
	
	def setLetra(self,letra):
		self.__letra=letra
		
	def setValor(self,valor):
		self.__valor=valor
	
	def setEstado(self,estado):
		self.__estado=estado
		
	def setImagen(self,letra):
		self.__imagenAnt=self.__imagenAct
		self.__imagenAct='./letras/'+letra+'.png'	
		
	def getLetra(self):
		return self.__letra
		
	def getValor(self):
		return self.__valor
		
	def getEstado(self):
		return self.__estado
		
	def getImagenAct(self):
		return self.__imagenAct
	
	def getImagenAnt(self):
		return self.__imagenAnt				
