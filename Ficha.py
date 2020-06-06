letras={1:['A','E','O','S','I','U','N','L','R','T'],2:['C','D','G'],3:['M','B','P'],4:['F','H','V','Y'],6:['J'],8:['K','LL','Ñ','Q','RR','W','X'],10:['Z']}

class Ficha():
	def __init__(self,letra):
		'''Recibe una letra como parámetro y a partir de esa letra, asigna el valor correspondiente'''		
		self.__letra=letra
		for key in letras.keys():
			if(letra in letras[key]):
				self.__valor=key
		self.__image='./letras/'+letra+'.png'		
	
	def getValor(self):
		return self.__valor
	
	def getLetra(self):
		return self.__letra
	
	def getImage(self):
		return sefl.__image

