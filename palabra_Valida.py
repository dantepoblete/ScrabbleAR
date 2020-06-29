from pattern.text.es import lexicon, spelling,parse

adj=["AO", "JJ","AQ","DI","DT"]
sus=["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"]
verb=[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG",  "VSI","VSN", "VSP","VSS"  ]

def clasificar(palabra,nivel):
	'''clasifica si la palabra es valida para el nivel seleccionado'''
	pal = parse(palabra).split()
	if (nivel=='facil'):
	   	if( pal in sus or adj or verb):
		     return True
	elif ((nivel=='medio')or (nivel=='dificil')):
		if( pal in  adj or verb):
			 return True
	else:
    	 return False

def palabra_Valida(palabra,nivel):
	'''A partir de la palabra ingresada en el tablero
	        chequea si es correcta o no'''
	ok=False
	if(((len(palabra))>=2) and ((len(palabra))<=7)):
		palabra=palabra.lower()
		if ((palabra in spelling) or (palabra in lexicon)):
    		 if(clasificar(palabra,nivel)):
    			 ok=True
	return ok
