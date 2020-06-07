import PySimpleGUI as sg
from Bolsa import Bolsa
from Ficha import Ficha

#---------Valores por defecto---------#
normal='./img/N.png' #Casilla normal del tablero.
unknown='./letras/NN.png' #Casillas ocultas del atril de la CPU.
import PySimpleGUI as sg
from Bolsa import Bolsa
from Ficha import Ficha

#---------Valores por defecto---------#
normal='./img/N.png' #Casilla normal del tablero.
unknown='./letras/NN.png' #Casillas ocultas del atril de la CPU.
cantFichas=7

#-------------------------------------#
bolsa=Bolsa()
bolsa.inicializar_Bolsa()
fichas=bolsa.getFichas()
	
#--------Tablero---------#
def crear_tablero(matriz):
    cantX=cantY=15
    for j in range(cantX):
        matriz.append([])
        for i in range(cantY):
            matriz[j].append(sg.Button(image_filename=normal, image_size=(35,35), key='-pos-', pad=(0,0)))

def crear_atriles(tablero):
    tablero.append([])
    tablero[1].append(sg.Frame(layout=[atrilCPU], title="atril CPU"))
    tablero[1].append(sg.Frame(layout=[atrilJugador], title="Atril Jugador"))

def dibujar_tablero():
    matriz=[]
    crear_tablero(matriz)
    tablero=[[sg.Frame(layout=matriz, title="Tablero")]]
    crear_atriles(tablero)
    return tablero

#---------Atril CPU---------#	

atrilCPU=[sg.Button(image_filename=unknown, image_size=(37,37),pad=(0,0)) for i in range(cantFichas)]

#---------Atril Jugador---------#

atrilJugador=[sg.Button(image_filename=fichas[i].getImage(), image_size=(37,37), pad=(0,0)) for i in range(cantFichas)]



tablero = dibujar_tablero()
window = sg.Window("ScrabbleAR",tablero)
event, values=window.read()
window.close()
