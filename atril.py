from Bolsa import Bolsa

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
     #Quita una ficha del atril
        self.__atril.remove(ficha)

    def get_espaciosLibres(self):
     #Cantidad de fichas que faltan en el atril
        return (7 - len(self.__atril))

    def get_Cantidad(self):
        return len(self.__atril)

    def rellenar_atril(self):
        while ((self.get_espaciosLibres() > 0)and(self.__bolsa.cantidad_fichas() > 0)):
             self.agregar_ficha()
             
    def get_atril(self):
        return self.__atril


