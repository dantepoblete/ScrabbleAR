import json
import PySimpleGUI as sg
from time import  strftime

background = sg.LOOK_AND_FEEL_TABLE['DarkBlue']['BACKGROUND']             

class Top():
    """ Clase que maneja el ranking de jugadores ordenaos por puntajes"""
    def __init__(self,file):
        self.__file = file
        self.__top10 = []

    def file(self):
        return self.__file

    def crearArchivo(self):
        try:
            #Si el archivo existe
            file = open(self.__file,"r")
            data = json.load(file)
            self.__top10 = data
            file.close()
        except:
            #Si el archivo no existe
            file = open(self.__file,"x")
            file.close()
        finally:
            return self.__top10


    def agregarNuevoPuntaje(self,jugador,cant_puntos,nivel):
        """Agrega al archivo los datos del jugador """
        puntajes = self.crearArchivo()
        if(len(puntajes) < 10):
            file = open(self.__file,"w")
            puntaje = {
                "jugador": jugador,
                "fecha": strftime("%d/%m/%Y"),
                "puntaje": cant_puntos,
                "nivel": nivel,
            }
            puntajes.append(puntaje)
            puntajes = sorted(puntajes, key = lambda i: i["puntaje"], reverse = True)
            json.dump(puntajes,file,indent=4)               
            file.close()
        else:
            file = open(self.__file,"w")
            puntaje = {
                 "jugador":jugador,
                 "fecha": strftime("%d/%m/%Y"),
                 "puntaje": cant_puntos,
                 "nivel": nivel,
                }
            puntajes[-1] = puntaje
            puntajes = sorted(puntajes, key = lambda i: i["puntaje"], reverse = True)
            json.dump(puntajes,file,indent=4)
            file.close()
     
    def mostrarTop(dato):
        ##Se obtienen los puntajes
        ranking= Top(dato)
        puntajes = ranking.crearArchivo()
        sg.change_look_and_feel('DarkBlue')
        ### Instanciacion de las columnas
        col_nombre = [[sg.Text("NOMBRE",text_color='white',background_color= background)]]
        col_puntaje =[[sg.Text("PUNTAJE",text_color='white',background_color= background)]]
        col_nivel = [[sg.Text("NIVEL",text_color='white',background_color= background)]]
        col_fecha = [[sg.Text("FECHA",text_color='white',background_color=background)]]
        ##Se agregan los datos correspondientes a cada columna
        for p in puntajes:
            col_nombre.append([sg.Text(p["jugador"])])
            col_puntaje.append([sg.Text(str(p["puntaje"]))])
            col_nivel.append([sg.Text(p["nivel"])])
            col_fecha.append([sg.Text(p["fecha"])])
        layout = [[sg.Column(col_nombre, element_justification='center'),sg.Column(col_puntaje, element_justification='center')
            ,sg.Column(col_nivel, element_justification='center'),sg.Column(col_fecha, element_justification='center')]]
        return layout
    
    def main():
        niveles = [[sg.Button('Facil',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='EASY'),
				sg.Button('Medio',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='MID'),
				sg.Button('Dificil',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='HARD'),
                sg.Button('General',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='TOTAL')
                ]]
        panel=mostrarTop("TopNiveles.json")
        layout = [[sg.Column(niveles)],[sg.Column(panel)]]
        menuRanking= sg.Window('Configuracion ScrabbleAR',layout)
        event,values=menuRanking.Read()
        menuRanking.close()
           
    if __name__ == '__main__':
        main()