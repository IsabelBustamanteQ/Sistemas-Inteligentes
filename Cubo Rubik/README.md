# Programa para Resolver Cubos Rubik 3x3
## 1.Nombre: 
Isabel Bustamante Quiroz
## 2. Descripción del Proyecto
El proyecto es un programa que te permite leer un cubo rubik a partir de un archivo de texto y te da instrucciones de cómo resolverlo.
## 3. Requerimientos de Entorno
El presente proyecto se realizó en un entorno Python 3.11.5
Se recomienda tener al menos 8GB de RAM para disminuir problemas en el uso de memoria del programa
## 4. Manual de Uso
### 4.1 Formato de codificacion para cargar el estado de un cubo desde un archivo de texto
El formato necesario para cargar el archivo de texto debe contar con 18 líneas, cada una debe contener 3 letras mayúsculas separadas por " " (espacio). 
Al finalizar cada línea, asegurese de no tener espacios o separaciones al final o al inicio del archivo de texto.
las letras válidas son las siguientes:
* "W"(blanco)
* "O" (anaranjado)
* "G" (verde)
* "R" (rojo)
* "B" (azul)
* "Y" (amarillo)
#### Ejemplo de archivo para leer el cubo:
A continuació se muestra el contenido que debe encontrarse en el archivo a leer.
Si deseas ver más ejemplos, revisa los archivos cube0.txt, cube1.txt y cube2.txt de este repositorio.
W W W

W W W

W W W

O O O

O O O

O O O

G G G

G G G

G G G

R R R

R R R

R R R

B B B

B B B

B B B

Y Y Y

Y Y Y

Y Y Y
### 4.2 Instrucciones para ejecutar el programa
El programa cuenta con un menú simple de 4 opciones. Al iniciar el programa se crea un objeto cubo que por defecto se encuentra armado.
#### 1. Leer cubo de archivo
Al escoger la opcion "1", el programa te pedirá que escribas la ruta donde se encuentra el archivo. Tras escribir el nombre del archivo, el programa hará las validaciones necesarias para asegurar que el archivo que lee, contiene una configuracion de cubo válida. 
Si la carga es exitosa, aparecerá el mensaje "El cubo fue cargado exitosamente".
Si hubo un error el la carga, el programa te avisará de que error se trata y tendrás el cubo armado por defecto.
#### 2. Mostrar el cubo
Al escoger la opcion "2", el programa mostrará el cubo que tiene actualmente, separando las caras con líneas punteadas.
#### 3. Resolver cubo
Al escoger la opcion "3", el programa empezará a buscar una solución al cubo que fue cargado anteriormente.
En caso de que el cube esté armado, te mostrará el mensaje "El cubo ya está armado"
**Nota:** 
* Esta opcion no modifica el cubo que se encuentra cargado, sólo muestra la solución.
* Si el cubo es muy dificil de armar puede tardar más de 20 minutos en encontrar la solución.
* Si deseas cancelar la ejecución del programa, presiona Ctrl+c
#### 0. Salir
Al escoger la opcion "0", el programa finaliza.
## 5. Diseño e implementación
### 5.1.Breve descripción de modelo del problema
El programa consta de 3 clases que nos permiten abarcar el problema en 3 pasos simples
* Leer un archivo correcto
    * Para leer el archivo, se utiliza la funcion load_cube() de la clase Rubik_cube.py, la cual está apoyada en la case Validator.py para asegurarse que sea correcto.
* Mover el cubo
    * La abstracción del movimiento del cubo fue desarrollada en la clase Rubik_cube.py.
* Buscar solucion del cubo
    * La busqueda de la solución se realiza mediante la clase Solver.py, quien recibe un cubo y busca la solución e imprime los pasos realizados.
### Rubik_cube.py
En esta clase se encuentra la abstraccion del cubo rubik en una lista de matrices de numpy de dimesiones (6,3,3), aquí se encuentran implementadas las acciones para mover los datos del cubo, las heuristicas y la opción de cargar un cubo a partir de un archivo de texto.
### Validator.py
Es una clase que recibe la lista de matrices de numpy para validar que cuente con los requisitos mínimos de un cubo rubik, los cuales son:
* Tener únicamente las letras "W"(blanco),"O" (anaranjado),"G" (verde),"R" (rojo),"B" (azul) y "Y" (amarillo).
* No tener más de 9 ocurrencias por color.
### Solver.py
Es la clase que implementa algoritmos de busqueda en espacio de estados para encontrar la solución al cubo rubik así como mostrar las instrucciones para resolver el mismo.
### 5.2.Explicación y justificación de algoritmo(s), técnicas, heurísticas seleccionadas.
#### Rubik_cube.py
Para realizar los distintos movimientos, se implementó 3 funciones importantes.
##### `row_motion(self, sides_list, row)`:
Esta función recibe como parámetros la lista de los lados que se ven involucrados en el movimiento de una fila, así como el numero de fila que es girada.
Dentro de la funcion se itera en cada lado del __sides_list__ y se le asigna la fila del lado anterior. Al finalizar se cambia la fila faltante en la penúltima cara con la fila de la primera cara.
Esta función se usa para los movientos U, U', D, D', S y S'
##### `row_and_column_motion(self,sides,line_number,right):`:
Esta función recibe como parámetros la lista de los lados que se ven involucrados en el movimiento de filas y columnas, así como el número de linea que se girará y el parámetro right, que es un booleano que nos ayuda a definir como reorganizar los elementos según el giro que se da.
En esta función se distingue a las filas y columnas involucradas mediante su posición en la lista de caras involucradas __sides__.
* si se encuentra en posicion par, se obtiene una fila y se asigna a la columna de la cara anterior.
* Si es encuentra en posicion impar, se obtiene una columna que se asigna a una fila de la cara anterior.
Al finalizar se cambia la fila faltante en la penúltima cara con la columna de la primera cara.
Esta función se apoya del método `flip_line` para colocar los elementos en el orden correcto.
Esta función se usa para modelar los movimientos F, F', B, B', S y S'
##### `column_motion(self,sides, columns,right):`:
Esta función recibe como parámetros la lista de los lados que se ven involucrados en el movimiento de una columna, así como el numero de columna que es girada y el parametro right que nos permite determinar el correcto ordenamiento de los elementos girados.
Dentro de la funcion se itera en cada lado del __sides_list__ y se le asigna la columna del lado anterior. Al finalizar se cambia la columna faltante en la penúltima cara con la columna de la primera cara.
Esta función se apoya del método `flip_line` para colocar los elementos en el orden correcto.
Esta función se usa para los movientos "R", "R'","L", "L'","M" y "M'"
##### `flip_line(self,line,right)`:
Este método se encarga de invertir la línea que le es pasada siempre y cuando en rigth sea True, caso contrario, no invierte la línea.
Este nos permite convertir una línea [1,2,3] en [3,2,1] cuando right es True. 
##### `roll_side(self,side,rotation)`:
Este método se encarga de girar la cara que es rotada, este transpone la cara y la reordena según el eje que se le manda.
* Si el eje es 0, voltea la matriz verticalmente
* Si el eje es 1, voltea la matriz horizontalmente
#### Solver.py
##### `a_star_solve(self)`:
Este método se encarga de realizar la búsqueda de la solución para el cubo rubik mediante el uso del algoritmo A*.
Previamente se implementó la búsqueda BFS, sin embargo, al tener varios movimientos, deja de ser eficiente.
El algoritmo usa dos listas importantes, __open__ que es una cola de prioridad, y __closed__ que son los nodos visitados.
Mientras la lista __open__ contenga elementos, el algoritmo obtiene el mejor candidato de la misma lista mediante el uso de una heurística combinada y verifica si el cubo está resuelto, si es así, llama a la funcion `instructions_to_solve()` que se encarga de mostrar las instrucciones al usuario.
En caso de no haber resuelto el cubo, se expande a los siguientes movimientos o acciones disponibles y continúa la busqueda.
#### Heurísticas usadas
Para mejorar el rendimiento de la funcion `a_star_solve(self)`, se implementó el uso de 2 heurísticas dentro de la clase __Rubik_cube__
##### Piezas que no están en su lugar
Esta heurística se implentó en el método `misplaced_pieces()`, la cual se encarga de contar cuantas piezas no son iguales a la pieza central de cada cara.
##### Distancia Manhattan
Esta heurística se implentó en el método `manhattan_distance()`, la cual se encarga de calcular la distancia manhattan entre el estado actual del cubo Rubik al estado del cubo armado. 
Se recorre cada lado del cubo se calcula la diferencia con el estado del cubo armado y se suman las diferencias obtenidas.
### Heuristica Combinada
Esta es el resultado de la suma de las heuristicas anteriormente mencionadas, se la observa en la funcion `combined_heuristic()`.
Dentro de la clase __Solver__ se llama a esta heuristica dentro del método `heuristic()`
### 5.3.En caso de usar modelos lingüísticos, incluir los prompts clave.
Este trabajo se apoyó en el uso del modelo lingüístico ChatGPT para las siguientes implementaciones:
* Heuristica combinada
    Prompts usado: 
    * Cual es la mejor heuristica para armar un cubo rubik?
    * Puedes darme un ejemplo de la heuristica combinada?
* Resolver problemas al leer el archivo:
    Prompts usado: 
    * Mi funcion load_cube no esta leyedo todas las lineas del archivo: --- código ---
    * Porque no se lee el archivo completo?
* Correción de errores
    Prompts usado: 
    * Que significa este error: ---error de la consola---
## 6. Trabajo Futuro
Actualmente el proyecto funciona únicamente con cubos 3x3 y no cuenta con todas las validaciones necesarias.
### 6.1.Lista de tareas inconclusas y/o ideas para continuar con el proyecto
* Terminar la implementación de los movientos centrales S, S', M, M', E y E'
* Validar que las aristas del cubo sean correctas
* Refactorizar el código para admitir cubos más grandes.