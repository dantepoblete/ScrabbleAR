import json
import PySimpleGUI as sg
import os
from time import  strftime

background = sg.LOOK_AND_FEEL_TABLE['DarkBlue']['BACKGROUND']             


class Top():
    """ Clase que maneja el ranking de jugadores ordenados por puntajes"""
    def __init__(self,filepath):
        self.__filepath = filepath
        self.__top10 = []

    def filepath(self):
        return self.__filepath

    def crearArchivo(self):
        try:
            os.mkdir('top')
        except(FileExistsError):
            pass	
        try:
            #Si el archivo existe
            file = open(self.__filepath,"r")
            data = json.load(file)
            self.__top10 = data
            file.close()
        except:
            #Si el archivo no existe
            file = open(self.__filepath,"x")
            file.close()
        finally:
            return self.__top10


    def agregarNuevoPuntaje(self,jugador,cant_puntos,nivel):
        """Agrega al archivo los datos del jugador de dos formas:
            -si el jugador no esta en el topTen se agrega  al archivo.
            -si el jugador ya esta en el ranking,si su puntaje es 
             mayor o igual se actualiza su puntaje  y la fecha."""
        puntajes = self.crearArchivo()
        if(len(puntajes) < 10):
            file = open(self.__filepath,"w")
            puntaje = {
                "jugador": jugador,
                "fecha": strftime("%d/%m/%Y"),
                "puntaje": cant_puntos,
                "nivel": nivel,
            }
            ok=False
            for jug in puntajes:
                if(ok==False):
                    if((jug["jugador"] == jugador) and(jug["nivel"]==nivel)):
                        if(cant_puntos >= jug["puntaje"]):
                            jug["puntaje"]=cant_puntos
                            jug["fecha"]=puntaje["fecha"]
                            ok=True       
            if(ok==False):
                 puntajes.append(puntaje)                           
            
            puntajes = sorted(puntajes, key = lambda i: i["puntaje"], reverse = True)
            json.dump(puntajes,file,indent=4)               
            file.close()
        else:
            file = open(self.__filepath,"w")
            puntaje = {
                 "jugador":jugador,
                 "fecha": strftime("%d/%m/%Y"),
                 "puntaje": cant_puntos,
                 "nivel": nivel,
                }
            ok=False
            for jug in puntajes:
                 if(ok==False):
                    if((jug["jugador"]== jugador) and(jug["nivel"]==nivel)):
                        if(cant_puntos >= jug["puntaje"]):
                            jug[puntaje]=cant_puntos
                            jug["fecha"]=puntaje["fecha"]
                            ok=True       
            if((ok==False)and(cant_puntos > puntajes[-1]["puntaje"])):                
                puntajes[-1]=puntaje                       
            
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
    ##Se agrega de forma dinamica los datos correspondientes a cada columna
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
    ]]
	panel=mostrarTop('./top/TopNiveles.json')
	selectNivel = [[sg.Frame('Seleccionar Nivel',niveles)]]
	topTen = [[sg.Frame('TopTen General',panel)]]#Muestro las puntuaciones del nivel General
	layout = [[sg.Column(selectNivel)],[sg.Column(topTen)]]
	menuRanking= sg.Window('TopTen General ScrabbleAR', layout, use_default_focus=False)
	while True:
		event,values = menuRanking.Read()
		if event == 'MID':
			#Creo una ventana con las puntuaciones correspondientes al nivel Medio
			panelMedio = mostrarTop('./top/TopMedio.json')
			layoutMed = [[sg.Column(panelMedio)]]
			winMed = sg.Window('TopTen Dificultad Medio',layoutMed)
			event,values=winMed.Read()
			winMed.Close()
		elif event == 'EASY':
			#Creo una ventana con las puntuaciones correspondientes al nivel Facil
			panelFacil = mostrarTop('./top/TopFacil.json')
			layoutFacil = [[sg.Column(panelFacil)]]
			winFacil = sg.Window('TopTen Dificultad Facil',layoutFacil)
			event,values=winFacil.Read()
			winFacil.Close()
		elif event == 'HARD':
			#Creo una ventana con las puntuaciones correspondientes al nivel Dificil
			panelDif = mostrarTop('./top/TopDificil.json')
			layoutDif = [[sg.Column(panelDif)]]
			winDif = sg.Window('TopTen Dificultad Dificil',layoutDif)
			event,values=winDif.Read()
			winDif.Close()
		else:
			break			
	menuRanking.close()
           
if __name__ == '__main__':
	main()
