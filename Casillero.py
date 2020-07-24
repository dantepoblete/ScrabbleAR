class Casillero():
	'''Esta clase representa un casillero del tablero, posee 6 atributos:
		pos:Indica la posicion del casillero.
		tipo:Indica el tipo de casillero(premio,descuento,normal,inicio)
		letra:Si se coloco una ficha, posee la letra correspondiente a la ficha.
		valor:Es el valor de la ficha colocada.
		imagenAnt,imagenAct:Poseen el nombre de la imagen del casillero antes y despues de colocarse una ficha.
	'''	
	def __init__(self,i,j,tipo):
		self.__pos=(i,j)
		self.__tipo=tipo
		self.__letra=''
		self.__valor=0
		self.__imagenAct='./img/'+self.__tipo+'.png'
		self.__imagenAnt=''
		
	def getPos(self):
		return self.__pos	
	
	def setLetra(self,letra):
		self.__letra=letra
		
	def setValor(self,valor):
		self.__valor=valor
	
	def setEstado(self,estado):
		self.__estado=estado
		
	def setImagen(self,imagen):
		self.__imagenAnt=self.__imagenAct
		self.__imagenAct=imagen
		
	def getLetra(self):
		return self.__letra
		
	def getValor(self):
		return self.__valor
		
	def getEstado(self):
		return self.__estado
		
	def getImagen(self):
		return self.__imagenAct
		
	def getTipo(self):
		return self.__tipo	
	
	def restoreImagen(self):
		self.__imagenAct=self.__imagenAnt
		self.__imagenAnt=''	
