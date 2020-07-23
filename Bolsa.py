import random
from Ficha import Ficha

class Bolsa:   
     def __init__(self):
         self.fichas= []
         self.inicializar_Bolsa()
     
     def agregar_Bolsa(self,letra,valor,cantidad):
          for i in range(cantidad):
               self.fichas.append(Ficha(letra,valor))
     
     def inicializar_Bolsa(self,dic):
          for letra in dic.keys():
               agregar_Bolsa(letra,dic[letra][0],dic[letra][1])
	  random.shuffle(self.fichas)
             
     def cantidad_fichas(self):
          #devuelve la cantidad de fichas restantes
          return len(self.fichas)    
     
     def tomar_ficha(self):
         #Toma la primera ficha de la bolsa y la elimina de la misma
         return self.fichas.pop()
     
     def getFichas(self):
         return self.fichas
    
