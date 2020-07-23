class Ficha():
	def __init__(self,letra,valor):
		self.__letra=letra
		self.__valor=valor
		self.__image='./letras/'+letra+'.png'	
	
	def getValor(self):
		return self.__valor
	
	def getLetra(self):
		return self.__letra
	
	def getImage(self):
		return self.__image

