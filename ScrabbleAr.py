import PySimpleGUI as sg
import Juego as Game
import webbrowser

sg.change_look_and_feel('LightBlue')

background = sg.LOOK_AND_FEEL_TABLE['LightBlue']['BACKGROUND']

def main(args):
	title = [sg.Button(image_filename = './img/LOGO.png', image_size = (491,285), button_color = ('white',background), border_width = 0)]
	options = [[sg.Button('Jugar',image_filename = './img/BT.png', image_size=(150,34), button_color=('white',background), border_width=0, key = ('-play-'))],
			  [sg.Button('Cargar Partida',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-load-'))],
			  [sg.Button('Puntuaciones',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-scores-'))],
			  [sg.Button('Salir',image_filename = './img/BT.png', image_size = (150,34),button_color = ('white',background), border_width = 0, key = ('-exit-'))]
			  ]
	information = [sg.Button(image_filename='./img/INFO.png', image_size=(30,30),tooltip='Mas información.', button_color=('white',background), border_width=0, key=('-info-')),sg.Text(7*('	')+'Grupo 15')]		  
			  
	panel = [title,[sg.Column(options,justification = "center")],information]		  

	menu = sg.Window('Menu Principal', panel, use_default_focus=False)
	
	while True:
		event,values = menu.Read()
		if event == '-play-':
			sg.change_look_and_feel('DarkBlue2')	#DarkTeal17
			Game.main()
		elif event == '-exit-':
			break
		elif event == '-info-':
			webbrowser.open('https://github.com/dantepoblete/ScrabbleAR', new = 2)	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
