from Bolsa import Bolsa
import PySimpleGUI as sg

#---------Ubicacion de imagen---------#
unknown='./letras/NN.png' #Casillas ocultas del atril de la CPU.

class Atril:
    
    def __init__(self):
        self.__bolsa=Bolsa()
        self.__atril=[]
        self.inicialiciar_atril()

    def agregar_ficha(self):
        self.__atril.append(self.__bolsa.tomar_ficha())

    def inicialiciar_atril(self):
         for i in range(7):
             self.agregar_ficha()
           

    def usar_ficha(self, ficha):
        #Quita una ficha determinada del atril
        self.__atril.remove(ficha)

    def get_espaciosLibres(self):
     #Cantidad de fichas que faltan en el atril
        return (7 - len(self.__atril))

    def get_Cantidad(self):
        return len(self.__atril)

    def rellenar_atril(self):
        while ((self.get_espaciosLibres() > 0)and(self.__bolsa.cantidad_fichas() > 0)):
             self.agregar_ficha()
             
    def get_atril_Jugador(self):
        lista=[]
        for i in range(self.get_Cantidad()):
             ficha=self.__atril[i]
             lista.append(sg.Button(image_filename=ficha.getImage(), image_size=(30,30),key=(ficha.getLetra(),ficha.getValor()), pad=(0,0)))
        return lista

    def get_atril_Cpu(self): 
        lista=[]
        for i in range(self.get_Cantidad()):
             ficha=self.__atril[i]
             lista.append(sg.Button(image_filename=unknown, image_size=(30,30),pad=(0,0)))
        return lista

    
    def cambiar_fichas (self,lista):
        cant=len(lista)
        for i in range(cant):
             self.__bolsa.agregar_Bolsa(lista[i].getLetra,1)               
        rellenar_atril(self)
    
