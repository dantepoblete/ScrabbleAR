![logo](/img/LOGO.png)

![](https://img.shields.io/github/license/dantepoblete/ScrabbleAR?style=plastic) ![](https://img.shields.io/static/v1?label=python&message=3.6.8&color=green&style=plastic) ![](https://img.shields.io/static/v1?label=pysimplegui&message=4.19+&color=red&style=plastic) ![](https://img.shields.io/static/v1?label=pattern&message=2.6&color=yellow&style=plastic) ![](https://img.shields.io/static/v1?label=plataforma&message=windows%207/8.1/10%20-%20linux&color=blue&style=plastic)
## Requisitos
* [Python 3.6.8](https://www.python.org/downloads/release/python-368/)
* [PySimpleGUI](https://github.com/PySimpleGUI)
* [Pattern](https://github.com/clips/pattern)
## Instalación
Luego de instalar la versión 3.6.8 de Python, usa [pip](https://pip.pypa.io/en/stable/) en la terminal de Windows o Linux para instalar los siguientes módulos:
```bash
pip install pysimplegui
```
```bash
pip install pattern
```
## Primeros Pasos

* Para iniciar el juego se debe correr el archivo **ScrabbleAR.py**

### Menu Principal
![](/img/Menu.JPG)
 * **Jugar:** *Empieza una nueva partida, si existe una partida guardada de un juego en progreso, puede elegir continuar.*
 * **Configuración:** *Modifica los parámetros del juego a tu gusto.*
 * **Puntuaciones:** *Un vistazo a los 10 mejores puntajes del juego, en general y por nivel.*

### Configuración
![](/img/Config.JPG)
* #### Nivel:
  ***Cada nivel posee un diseño de tablero diferente, acorde a la dificultad seleccionada.***
  * **Facil:** *Jugar con adjetivos,sustantivos,verbos.*
  * **Medio:** *Jugar con verbos y adjetivos.*
  * **Dificil:** *Jugar con verbos y adjetivos.*
* #### Configurar Fichas  
  * **Letra:** *Selecciona la letra de la que desees modificar sus parámetros.*
  * **Valor:** *Cambia el valor de la letra seleccionada.*
  * **Cantidad:** *El valor que selecciones, será la cantidad de fichas correspondientes a la letra seleccionada que aparecerán en la partida.*
* #### Tiempo de Partida: 
  * *Es el tiempo en minutos que durará la partida.*
* #### Aceptar:
  * *Guarda la configuracion del juego.*
* #### Predeterminado:
  * *Reestablece los valores por defecto de la configuración.*
  
## Dentro del Juego
  
 ### Atril
![](/letras/E.png)![](/letras/S.png)![](/letras/D.png)![](/letras/T.png)![](/letras/A.png)![](/letras/R.png)![](/letras/N.png)

*Son las fichas que el jugador dispone para utilizar en el tablero. A medida que se van utilizando, son reemplazadas por otras fichas procedentes de la bolsa.*
***Cada ficha posee un valor numerico que incidirá en el puntaje de la palabra***
 ### Casilleros
 
  ***Cada casillero posee una descripción. Ubicar el cursor sobre un casillero mostrará la característica del mismo.***
 
  * ![](/img/N.png) *Casillero* ***normal*** *del juego.*
  * ![](/img/IN.png) *Casillero de* ***inicio del juego***. *Coloca una ficha en él para empezar a jugar.*
 #### Casilleros con Premios
  * ![](/img/DL.png) ***Duplica*** *el valor de una ficha.*
  * ![](/img/TL.png) ***Triplica*** *el valor de una ficha.*
  * ![](/img/DP.png) ***Duplica*** *el valor de una palabra.*
  * ![](/img/TP.png) ***Triplica*** *el valor de una palabra.*
 #### Casilleros con Descuentos
  * ![](/img/P1.png) ***Resta*** *1 punto a una palabra.*
  * ![](/img/P2.png) ***Resta*** *2 puntos a una palabra.*
  * ![](/img/P3.png) ***Resta*** *3 puntos a una palabra.*
 ### Acciones
  * #### Validar
    ![](/img/VAL.png)
    
    *Luego de formar una palabra, al pulsar este botón se determinará si es valida (según el nivel). Si resulta valida,*
    *la palabra formada permanecerá en el tablero y el puntaje correspondiente será asignado al jugador*.***En caso contrario***
    ***las fichas utilizadas serán devueltas al atril.***
  * #### Cambiar Fichas
    ![](/img/CF.png)
   
    *Si el jugador lo desea puede cambiar las fichas presentadas en su atril por otras dentro de la bolsa. Una vez pulsado*
    *este botón, seleccione las fichas a cambiar y luego vuelva a pulsar el botón para confirmar el cambio.*
    ***El jugador solo dispone de 3 cambios en toda la partida.***
  * #### Posponer Partida
    ![](/img/POS.png)
    
    *El jugador puede guardar el estado de la partida actual para ser reanudada posteriormente, al presionar este botón.*
    ***Si ya existe una partida guardada, la misma será sobreescrita.***
  * #### Finalizar Partida
    ![](/img/FIN.png)
    
    *Si el jugador ya no desea continuar con la partida, solo basta con pulsar este botón para* ***finalizar el juego.***
  * #### Ceder Turno
    ![](/img/BT2.png)
    
    *El jugador le cede su turno a la IA al pulsar este botón.*
 ## Integrantes
 * [Link, Agustín Nicolas.](https://github.com/aguslink97)
 * [Poblete, Dante José.](https://github.com/dantepoblete)
 ## Recursos
 * [Python 3.6.8](https://www.python.org/downloads/release/python-368/) - *Lenguaje utilizado*
 * [PySimpleGUI](https://github.com/PySimpleGUI) - *Interfaz gráfica de usuario empleada.*
 * [Pattern](https://github.com/clips/pattern) - *Procesamiento de palabras*
 * **Adobe Photoshop** - *Herramienta empleada para el diseño/creación de las imagenes del juego.*
 ## Licencia
 * Este proyecto cuenta con [Licencia GPL 3.0](/LICENSE.md)
 
