import PySimpleGUI as sg
from Bolsa import Bolsa
from Ficha import Ficha

#---------Valores por defecto---------#
normal='./img/N.png' #Casilla normal del tablero.
unknown='./letras/NN.png' #Casillas ocultas del atril de la CPU.
cantX=cantY=15
cantFichas=7
#-------------------------------------#

bolsa=Bolsa()
bolsa.inicializar_Bolsa()
fichas=bolsa.getFichas()

#---------Tablero---------#

tablero=[[sg.Button(image_filename=normal, image_size=(35,35), key='-pos-', pad=(0,0)) for j in range(cantX)] for i in range(cantY)]
	
#---------Atril CPU---------#	

atrilCPU=[sg.Button(image_filename=unknown, image_size=(35,35),pad=(0,0)) for i in range(cantFichas)]

#---------Atril Jugador---------#

atrilJugador=[sg.Button(image_filename=fichas[i].getImage(), image_size=(35,35),key=(fichas[i].getLetra(),fichas[i].getValor()), pad=(0,0)) for i in range(cantFichas)]

#---------Ventana---------#
Interfaz=[[sg.Text('Atril CPU ')],
	   atrilCPU,
           [sg.Text('Tablero')],
           [sg.Column(tablero)],
           [sg.Text('Atril Jugador ')],
	   atrilJugador
      ]
window = sg.Window('Scrabble').Layout(Interfaz) 
window = sg.Window('ScrabbleAR', layout)
event,values=window.read()
window.close()
	
