![](/img/LOGO.png)
# Requisitos
* [Python 3.6.8](https://www.python.org/downloads/release/python-368/)
* [PySimpleGUI](https://github.com/PySimpleGUI)
* [Pattern](https://github.com/clips/pattern)
# Instalación
Luego de instalar la versión 3.6.8 de Python, usa [pip](https://pip.pypa.io/en/stable/) para instalar los siguientes módulos:
```bash
pip install pysimplegui
```
```bash
pip install pattern
```
# Primeros Pasos

## Menu Principal
![](/img/Menu.JPG)
 * **Jugar:** *Empieza una nueva partida, si existe una partida guardada de un juego en progreso, puede elegir continuar.*
 * **Configuración:** *Modifica los parámetros del juego (nivel,fichas,tiempo) a tu gusto.*
 * **Puntuaciones:** *Un vistazo a los 10 mejores puntajes del juego, en general y por nivel.*

## Configuración
![](/img/Config.JPG)
* ### Nivel:
  ***Cada nivel posee un diseño de tablero diferente, acorde a la dificultad seleccionada.***
  * **Facil:** *Jugar con adjetivos,sustantivos,verbos*
  * **Medio:** *Jugar con verbos y sustantivos*
  * **Dificil:** *Jugar con una categoría al azar*
* ### Configurar Fichas  
  * **Letra:** *Selecciona la letra de la que desees modificar sus parámetros.*
  * **Valor:** *Cambia el valor de la letra seleccionada.*
  * **Cantidad:** *El valor que selecciones, será la cantidad de fichas correspondientes a la letra seleccionada que aparecerán en la partida.*
* ### Tiempo de Partida : 
  * *Es el tiempo en minutos que durará la partida.*
  
# Dentro del Juego
  
 ## Atril
![](/letras/E.png)![](/letras/S.png)![](/letras/D.png)![](/letras/T.png)![](/letras/A.png)![](/letras/R.png)![](/letras/N.png)
**Son las fichas que el jugador dispone para utilizar en el tablero. A medida que se van utilizando, son reemplazadas por otras fichas procedentes de la bolsa.**
**Cada ficha posee un valor numerico que incidirá en el puntaje de la palabra**
 ## Casilleros
  * ![](/img/N.png) **Casillero normal del juego.**
  * ![](/img/IN.png) **Casillero de inicio del juego. Coloca una ficha en él para empezar a jugar.**
 ### Casilleros con Premios
  * ![](/img/DL.png) **Duplica el valor de una ficha.**
  * ![](/img/TL.png) **Triplica el valor de una ficha.**
  * ![](/img/DP.png) **Duplica el valor de una palabra.**
  * ![](/img/TP.png) **Triplica el valor de una palabra.**
 ### Casilleros con Descuentos
  * ![](/img/P1.png) **Resta 1 punto a una palabra.**
  * ![](/img/P2.png) **Resta 2 puntos a una palabra.** 
  * ![](/img/P3.png) **Resta 3 puntos a una palabra.**
 ## Acciones
  * ### Validar
    ![](/img/VAL.png)
    **Luego de formar una palabra, al pulsar este botón se determinará si es valida (según el nivel). Si resulta valida,**
    **la palabra formada permanecerá en el tablero y el puntaje correspondiente será asignado al jugador. En caso contrario**
    **las fichas utilizadas serán devueltas al atril.**
  * ### Cambiar Fichas
    ![](/img/CF.png)
    **Si el jugador lo desea puede cambiar las fichas presentadas en su atril por otras dentro de la bolsa. Una vez pulsado**
    **este botón, seleccione las fichas a cambiar y luego vuelva a pulsar el botón para confirmar el cambio.**
  * ### Posponer Partida
    ![](/img/POS.png)
    **El jugador puede guardar el estado de la partida actual para ser reanudada posteriormente, al presionar este botón.**
    ***Si ya existe una partida guardada, la misma será sobreescrita***
  * ### Finalizar Partida
    ![](/img/FIN.png)
    **Si el jugador ya no desea continuar con la partida, solo basta con pulsar este botón**
 # Integrantes
 * [Link, Agustín Nicolas.](https://github.com/aguslink97)
 * [Poblete, Dante José.](https://github.com/dantepoblete)
