import PySimpleGUI as sg
import functs.Juego as Game
import objetos.Configuracion as Configuracion
from objetos.Configuracion import Config
import objetos.TopTen as Top
import webbrowser

sg.change_look_and_feel('LightBlue')

background = sg.LOOK_AND_FEEL_TABLE['LightBlue']['BACKGROUND']

def main(args):
	title = [sg.Image(filename = './img/LOGO.png', size = (491,285), background_color = background)]
	options = [[sg.Button('Jugar',image_filename = './img/BT.png', image_size=(150,34), button_color=('white',background), border_width=0, key = ('-play-'))],
			   [sg.Button('Configuracion',image_filename = './img/BT.png', image_size=(150,34), button_color=('white',background), border_width=0, key = ('-config-'))],
			   [sg.Button('Puntuaciones',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-scores-'))],
			   [sg.Button('Salir',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-exit-'))],
			  ]
	information = [sg.Button(image_filename='./img/INFO.png', image_size=(30,30),tooltip='Mas información.', button_color=('white',background), border_width=0, key=('-info-')),sg.Text(7*('	')+'Grupo 15')]		  
			  
	panel = [title,[sg.Column(options,justification = "center")],information]		  

	menu = sg.Window('Menu Principal', panel, use_default_focus=False)
	
	configGame=Config()	#Configuracion por defecto del juego.
	
	while True:
		event,values = menu.Read()
		if event == '-play-':
			try:
				open('./save/PartidaGuardada.pckl')
				opcion = sg.PopupYesNo('Hay una partida guardada de un juego en progreso.\n¿Desea cargarla?',title='Cargar Partida')
				if(opcion == 'Yes'):
					Game.main(configGame,True)
				else:
					Game.main(configGame)	
			except(FileNotFoundError):
				Game.main(configGame)			
		elif event == '-config-':
			Configuracion.main(configGame)
		elif event == '-exit-':
			break
		elif event == '-scores-':
			Top.main()
		elif event == '-info-':
			webbrowser.open('https://github.com/dantepoblete/ScrabbleAR', new = 2)	
		else:
			break
		sg.change_look_and_feel('LightBlue')		

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
