import PySimpleGUI as sg

background = sg.LOOK_AND_FEEL_TABLE['LightBlue']['BACKGROUND']

letras = ('A','B','C','D','E','F','G','H','I','J','K','L','LL','M','N','Ñ','O','P','Q','R','RR','S','T','U','V','W','X','Y','Z')

valores = (1,2,3,4,6,8,10)

cantidad = (1,2,3,4,5,6,7,8,9,10,11)

fichasAgregadas=0 #Como se configura la cantidad de fichas, esta variable controla que no se agreguen mas de 100 fichas.

def main():
	niveles = [[sg.Button('Facil',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='EASY'),
				sg.Button('Medio',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='MID'),
				sg.Button('Dificil',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='HARD')
			  ]]

	selectLetras = [[sg.Text('Letra')],[sg.Spin(values=letras, size=(3,1),initial_value=letras[0], key='LET')]]
	selectValores = [[sg.Text('Valor')],[sg.Spin(values=valores, size=(3,1),initial_value=valores[0], key='VAL')]]
	selectCantidad = [[sg.Text('Cantidad')],[sg.Spin(values=cantidad, size=(3,1),initial_value=cantidad[0], key='CANT')]]
	agregarFichas = [[sg.Button('Agregar Fichas',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key='ADD')]]
	selectTiempo=[[sg.Slider(range=(1,15), orientation='h', size=(30, 20), default_value=8, key='TIME')]]
	selectCambios=[[sg.Slider(range=(1,5), orientation='h', size=(30, 20), default_value=3, key='CAMB')]]
	panelUno = [[sg.Column(selectLetras),sg.Column(selectValores),sg.Column(selectCantidad)],[sg.Column(agregarFichas)]]

	configUno = [[sg.Frame('Configurar Nivel',niveles)]]
	configDos = [[sg.Frame('Configurar Fichas',panelUno)]]
	configTres = [[sg.Frame('Configurar Tiempo de Juego (en minutos)',selectTiempo)]]
	configCuatro = [[sg.Frame('Configurar Cambios',selectCambios)]]
	
	opciones = [[sg.Button('Aceptar',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key ='OK'),
				sg.Button('Cancelar',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key ='CANCEL'),
				sg.Button('Predeterminado',image_filename = './img/BT2.png', image_size = (120,27),button_color = ('white',background), border_width = 0, key ='DEFAULT')
			  ]]
	
	layout = [[sg.Column(configUno)],[sg.Column(configDos)],[sg.Column(configTres)],[sg.Column(configCuatro)],[sg.Column(opciones)]]

	window= sg.Window('Configuracion ScrabbleAR',layout, use_default_focus=False)

	while True:
		event,values=window.Read()

if __name__ == '__main__':
    main()
	



