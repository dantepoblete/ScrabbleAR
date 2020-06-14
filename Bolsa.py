import random
from Ficha import Ficha

class Bolsa:   
     def __init__(self):
         self.fichas= []

     def agregar_Bolsa(self,letra,cantidad):
         for i in range(cantidad):			  
              self.fichas.append(Ficha(letra))

     def inicializar_Bolsa(self):
             self.agregar_Bolsa('A', 11)
             self.agregar_Bolsa('B', 3)
             self.agregar_Bolsa('C', 4)
             self.agregar_Bolsa('D', 4)
             self.agregar_Bolsa('E', 11)
             self.agregar_Bolsa('F', 2)
             self.agregar_Bolsa('G', 2)
             self.agregar_Bolsa('H', 2)
             self.agregar_Bolsa('I',6)
             self.agregar_Bolsa('J', 2) 
             self.agregar_Bolsa('K', 1)      
             self.agregar_Bolsa('L', 4)
             self.agregar_Bolsa('LL', 1)
             self.agregar_Bolsa('M', 3)
             self.agregar_Bolsa('N', 5)
             self.agregar_Bolsa('O', 8)
             self.agregar_Bolsa('P', 2)
             self.agregar_Bolsa('Q', 1)
             self.agregar_Bolsa('R', 4)
             self.agregar_Bolsa('RR', 1)
             self.agregar_Bolsa('S', 7)
             self.agregar_Bolsa('T', 4)
             self.agregar_Bolsa('U', 6)
             self.agregar_Bolsa('V', 2)
             self.agregar_Bolsa('X', 1)
             self.agregar_Bolsa('W', 1)
             self.agregar_Bolsa('Y', 1)
             self.agregar_Bolsa('Z', 1)
             random.shuffle(self.fichas)
             
     def cantidad_fichas(self):
          #devuelve la cantidad de fichas restantes
          return len(self.fichas)    
     
     def tomar_ficha(self):
         #Toma la primera ficha de la bolsa y la elimina de la misma
         return self.fichas.pop()
     
     def getFichas(self):
         return self.fichas
    
