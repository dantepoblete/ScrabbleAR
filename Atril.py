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
		'''Repongo las fichas utilizadas del atril por otras de la bolsa.Si se acabaron las fichas de
		la bolsa, guardo en una lista la posicion de las fichas que no puedieron reponerse'''
		noRepuestas=[]
		for i in pos:
			if(self.__bolsa.cantidad_fichas()!=0):
				self.__listaFichas[i] = self.__bolsa.tomar_ficha()
			else:
				noRepuestas.append(i)
				pos.remove(i)
		return noRepuestas		
				
	def finalizarAtril(self):
		if(self.__bolsa.cantidad_fichas() == 0):
			return True
		else:
			return False
						
	def puntajeFinal(self,noRepuestas):
		'''Devuelvo el puntaje sumado de todas las fichas que quedaron en el atril'''
		tot=0
		for ficha in self.__listaFichas:
			#Solo cuento las fichas presentes.
			if(self.__listaFichas.index(ficha) not in noRepuestas):
				tot+=ficha.getValor()
		return tot	
			
	def getImagen(self,i):
		return self.__listaFichas[i].getImage()
		
	def getLetra(self,i):
		return self.__listaFichas[i].getLetra()
		
	def getValor(self,i):
		return self.__listaFichas[i].getValor()

	def getFicha(self,i):
		return self.__listaFichas[i]
	
	def cambiarFichas(self,fichas):
		self.completarAtril(fichas)
		for i in fichas:
	   		self.__bolsa.agregar_Bolsa(self.getLetra(i),self.getValor(i),1)
