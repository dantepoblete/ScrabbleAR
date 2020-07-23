from Bolsa import Bolsa

class Atril:
	def __init__(self,dic):
		self.__bolsa = Bolsa(dic)
		self.__listaFichas = []
        
	def inicializarAtril(self):
		for i in range(7):
			self.__listaFichas.append(self.__bolsa.tomar_ficha())
	
	def completarAtril(self,pos):
		for i in pos:
			self.__listaFichas[i] = self.__bolsa.tomar_ficha()
			
	def completarAtrilCPU(self,palabra):
		for i in palabra:
			self.__listaFichas.append(self.__bolsa.tomar_ficha())		
			
	def getImagen(self,i):
		return self.__listaFichas[i].getImage()
		
	def getLetra(self,i):
		return self.__listaFichas[i].getLetra()
		
	def getValor(self,i):
		return self.__listaFichas[i].getValor()

	def getFicha(self,i):
		return self.__listaFichas[i]
		
	def getAtril(self):
		return self.__listaFichas
		
	def quitarFicha(self,ficha):
		self.__listaFichas.remove(ficha)	
	
	def cambiarFichas(self,fichas):
		self.completarAtril(fichas)
		for i in fichas:
	   		self.__bolsa.agregar_Bolsa(self.getLetra(i),1)
		
