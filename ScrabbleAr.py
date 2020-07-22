import PySimpleGUI as sg
import Juego as Game
import Configuracion as Config
import webbrowser

sg.change_look_and_feel('LightBlue')

background = sg.LOOK_AND_FEEL_TABLE['LightBlue']['BACKGROUND']

def main(args):
	title = [sg.Image(filename = './img/LOGO.png', size = (491,285), background_color = background)]
	options = [[sg.Button('Jugar',image_filename = './img/BT.png', image_size=(150,34), button_color=('white',background), border_width=0, key = ('-play-'))],
			   [sg.Button('Configuracion',image_filename = './img/BT.png', image_size=(150,34), button_color=('white',background), border_width=0, key = ('-config-'))],
			  [sg.Button('Cargar Partida',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-load-'))],
			  [sg.Button('Puntuaciones',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-scores-'))],
			  ]
	information = [sg.Button(image_filename='./img/INFO.png', image_size=(30,30),tooltip='Mas información.', button_color=('white',background), border_width=0, key=('-info-')),sg.Text(7*('	')+'Grupo 15')]		  
			  
	panel = [title,[sg.Column(options,justification = "center")],information]		  

	menu = sg.Window('Menu Principal', panel, use_default_focus=False)
	
	while True:
		event,values = menu.Read()
		if event == '-play-':
			sg.change_look_and_feel('DarkBlue2')
			Game.main()
		elif event == '-config-':
			Config.main()
		elif event == '-info-':
			webbrowser.open('https://github.com/dantepoblete/ScrabbleAR', new = 2)	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
