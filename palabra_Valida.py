from pattern.text.es import lexicon, spelling,parse

adj=["AO", "JJ","AQ","DI","DT"]
sus=["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"]
verb=[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG",  "VSI","VSN", "VSP","VSS"  ]


def clasificar(palabra):
    pal = parse(palabra).split()
    if pal in sus or adj or verb:
         return True
    else:
        return False   
   
	
def palabra_Valida(palabra):
    if(((len(palabra))>=2) and ((len(palabra))<=7)) :
         palabra=palabra.lower()
         if (palabra in spelling):
             return True
         elif(palabra in lexicon):
             return True
     else:
         return False        
  

  
