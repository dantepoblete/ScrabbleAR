from Bolsa import Bolsa
from Ficha import Ficha

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
	   		self.__bolsa.agregar_Bolsa(self.getLetra(i),self.getValor(i),1)
	   		
	def backUpAtril(self):
		backUpAtril=[]
		for ficha in self.__bolsa.getFichas():
			backUpAtril.append((ficha.getLetra(),ficha.getValor()))
		for ficha in reversed(self.__listaFichas):
			backUpAtril.append((ficha.getLetra(),ficha.getValor()))
		return backUpAtril
		
	def restaurarAtril(self,backUpAtril):
		fichas=[Ficha(ficha[0],ficha[1]) for ficha in backUpAtril]
		self.__bolsa.setBolsa(fichas)	
			
					   		
		
