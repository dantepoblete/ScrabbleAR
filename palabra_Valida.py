from pattern.text.es import lexicon, spelling,parse

adj=["AO", "JJ","AQ","DI","DT"]
sus=["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"]
verb=[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG",  "VSI","VSN", "VSP","VSS"  ]


def clasificar(palabra):
    pal = parse(palabra).split()
    if pal[0][0][1] in sus or adj or verb:
        esValida=True
    else:
        esValida=False   
    return esValida
	
	
def palabra_Valida(palabra):
     if(((len(palabra))>=2) and ((len(palabra))<=7)) :
         palabra=palabra.lower()
         if (not palabra in spelling):
             if (not palabra in lexicon):
	             esValida=False
	             return esValida  
             else:
                 esValida=clasificar(palabra)
                 print(esValida)     
                 return esValida    
         else:
	         esValida= clasificar(palabra)
	         print(esValida)
	         return esValida
     else:
         return False        

  