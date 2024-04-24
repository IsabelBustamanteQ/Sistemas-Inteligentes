# Programa para Resolver Cubos Rubik 3x3
## 1.Nombre: 
Isabel Bustamante Quiroz
## 2. Descripción del Proyecto
El proyecto es un programa que te permite leer un cubo rubik a partir de un archivo de texto y te da instrucciones de cómo resolverlo.
Consiste en 3 clases
### Rubik_cube.py
En esta clase se encuentra la abstraccion del cubo rubik en una lista de matrices de numpy, aquí se encuentran implementadas las acciones para mover los datos del cubo, las heuristicas y la opcion de cargar un cubo a partir de un archivo de texto.
### Validator.py
Es una clase que recibe la lista de matrices de numpy para validar que cuente con los requisitos mínimos de un cubo rubik, los cuales son:
- Tener únicamente las letras "W"(blanco),"O" (anaranjado),"G" (verde),"R" (rojo),"B" (azul) y "Y" (amarillo).
- No tener más de 9 ocurrencias por color.
### Solver.py
Es la clase que implementa el algoritmo de busqueda A* para encontrar la solución al cubo rubik.
## 3. Requerimientos de Entorno
El presente proyecto se realizó en un entorno Python 3.11.5
## 4. Manual de Uso
### 4.1 Formato de codificacion para cargar el estado de un cubo desde un archivo de texto
El formato necesario para cargar el archivo de texto debe contar con 18 líneas, cada una debe contener 3 letras mayúsculas separadas por " " (espacio). 
Al finalizar cada línea, asegurese de no tener espacios o separaciones al final o al inicio del archivo de texto.
las letras válidas son las siguientes:
- "W"(blanco)
- "O" (anaranjado)
- "G" (verde)
- "R" (rojo)
- "B" (azul)
- "Y" (amarillo)
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
### 4.2 Ins