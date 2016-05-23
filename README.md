# Fundamentos de los Sistemas Inteligentes

Nuestra heurística utiliza otras 4 funciones que calculan la heurística en una sola dirección, por ejemplo *“horizontal_heuristic”* calcula la heurística recorriendo todo el tablero, cuando se encuentra que en una posición dada hay una ficha de un jugador, se llama a la función *“horizontal_count”*, que cuenta cuantas fichas de ese mismo jugador están en línea **solo en horizontal**, a continuación se calcula que valor tiene utilizando la función *“get_horizontal_points”*, en esta función se tiene en cuenta si en ambos extremos de las fichas en línea hay una posición libre, o está ocupada por el contrario, además del número de fichas en línea, de forma que en cuanto más fichas en línea, mayor puntuación. Una vez calculada la puntuación se suma o resta al valor total dependiendo de si la ficha comprobada es del jugador problema o del contrincante.

Las otras tres funciones que utiliza *“combined_heuristic”*, *“vertical_heuristic”*, *“diagonal_heuristic”* y *“inverse_diagonal_heuristic”* funcionan de manera similar, pero atendiendo a otras direcciones.

vertical_heuristic → solo en vertical

diagonal_heuristic → diagonales desde posiciones de la parte inferior izquierda a la parte superior derecha

inverse_diagonal_heuristic → diagonales desde posiciones de la parte inferior derecha a la parte superior izquierda
Comparación de tiempos
----------------------------------
La partida y el código que se utilizo para capturar los tiempos se puede ver en el branch "compare_memoize_times"

  Sin memoize  -----------------Con memoize

1.94297194481 ------------- 1.18661999702

2.39799189568 ------------- 1.7296898365

2.61900091171 ------------- 1.76284599304

2.37093091011 ------------- 1.67776012421

2.83546805382 ------------- 1.93973016739

1.81011891365 ------------- 1.37647104263

3.44141697884 ------------- 2.23549008369

2.36817121506 ------------- 1.69369792938

2.87195205688 ------------- 1.92427706718

1.65478301048 ------------- 1.31733894348

2.21956992149 ------------- 1.83777403831

3.12181401253 ------------- 1.77787685394
