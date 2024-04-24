# Programa para Resolver Cubos Rubik 3x3
## 1.Nombre: 
Isabel Bustamante Quiroz
## 2. Descripción del Proyecto
El proyecto es un programa que te permite leer un cubo rubik a partir de un archivo de texto y te da instrucciones de cómo resolverlo.
## 3. Requerimientos de Entorno
El presente proyecto se realizó en un entorno Python 3.11.5
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
A continuacion se muestra el contenido que debe encontrarse en el archivo a leer, si deseas ver más ejemplos, revisa los archivos cube0.txt, cube1.txt y cube2.txt de este repositorio.
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
* * Para leer el archivo, se utiliza la funcion load_cube() de la clase Rubik_cube.py, la cual está apoyada en la case Validator.py para asegurarse que sea correcto.
* Mover el cubo
* * La abstracción del movimiento del cubo fue desarrollada en la clase Rubik_cube.py.
* Buscar solucion del cubo
* * La busqueda de la solución se realiza mediante la clase Solver.py, quien recibe un cubo y busca la solución e imprime los pasos realizados.
### Rubik_cube.py
En esta clase se encuentra la abstraccion del cubo rubik en una lista de matrices de numpy de dimesiones(6,3,3), aquí se encuentran implementadas las acciones para mover los datos del cubo, las heuristicas y la opcion de cargar un cubo a partir de un archivo de texto.
### Validator.py
Es una clase que recibe la lista de matrices de numpy para validar que cuente con los requisitos mínimos de un cubo rubik, los cuales son:
* Tener únicamente las letras "W"(blanco),"O" (anaranjado),"G" (verde),"R" (rojo),"B" (azul) y "Y" (amarillo).
* No tener más de 9 ocurrencias por color.
### Solver.py
Es la clase que implementa algoritmos de busqueda en espacio de estados para encontrar la solución al cubo rubik así como mostrar las instrucciones para resolver el mismo.
### 5.2.Explicación y justificación de algoritmo(s), técnicas, heurísticas seleccionadas.
#### Rubik_cube.py

#### Validator.py
Es una clase que recibe la lista de matrices de numpy para validar que cuente con los requisitos mínimos de un cubo rubik, los cuales son:
* Tener únicamente las letras "W"(blanco),"O" (anaranjado),"G" (verde),"R" (rojo),"B" (azul) y "Y" (amarillo).
* No tener más de 9 ocurrencias por color.
#### Solver.py
Es la clase que implementa algoritmos de busqueda en espacio de estados para encontrar la solución al cubo rubik así como mostrar las instrucciones para resolver el mismo.
### 5.3.En caso de usar modelos lingüísticos, incluir los prompts clave.
## 6. Trabajo Futuro
### 6.1.Lista de tareas inconclusas y/o ideas para continuar con el proyecto