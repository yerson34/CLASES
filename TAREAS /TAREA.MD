# TKINTER - LIBRERIA DE PYTHON PARA LA CREACION DE INTERFAZ GRAFICAS 
## *1. Introducción*
* Tkinter es el paquete más utilizado para crear interfaces gráficas en Python. Es una capa orientada a objetos basada en Tcl (sencillo y versátil lenguaje de programación open-source) y Tk (la herramienta GUI estándar para Tcl).

## *2. Entorno*
* El tutorial está escrito usando el siguiente entorno:

* Hardware: Portátil MacBook Pro 15′ (2.2 Ghz Intel Core i7, 16GB DDR3).
Sistema Operativo: Mac OS Mojave 10.14
Aplicación de desarrollo: Sublime Text 3.2.2
## *3. Widgets*
* A la hora de montar una vista con Tkinter, nos basaremos en widgets jerarquizados, que irán componiendo poco a poco nuestra interfaz. Algunos de los más comunes son:

* Tk: es la raíz de la interfaz, donde vamos a colocar el resto de widgets.
Frame: marco que permite agrupar diferentes widgets.
Label: etiqueta estática que permite mostrar texto o imagen.


* Entry: etiqueta que permite introducir texto corto (típico de formularios).


* Text: campo que permite introducir texto largo (típico para añadir comentarios).


* Button: ejecuta una función al ser pulsado.


* Radiobutton: permite elegir una opción entre  varias.


* Checkbutton: permite elegir varias de las opciones propuestas.


* Menu: clásico menú superior con opciones (Archivo, Editar…).


* Dialogs: ventana emergente (o pop-up).


* Cuando vayamos a inicializar el componente, debemos pasar por constructor el elemento que quede “por encima” en la jerarquía de la vista (si queremos colocar una label dentro de un frame, al construir la etiqueta le pasaremos el marco como argumento del constructor).

## *4. Configuración*
* Para configurar un widget, simplemente llamamos a .config() y pasamos los argumentos que queramos modificar. Algunas opciones son:

bg: modifica el color de fondo. Se puede indicar con el color en inglés (incluyendo modificadores, como “darkgreen”) o su código RGB en hexadecimal (“#aaaaaa” para blanco). Ojo: en MacOS no se puede modificar el color de fondo de los botones; aunque indiquemos un nuevo color, se mostrará en blanco. Lo más parecido que podemos hacer es configurar el highlightbackground, que pintará el fondo alrededor del botón del color que indiquemos.
fg: cambia el color del texto.
cursor: modifica la forma del cursor. Algunos de los más utilizados son “gumby”, “pencil”, “watch” o “cross”.
height: altura en líneas del componente.
width: anchura en caracteres del componente.
font: nos permite especificar, en una tupla con nombre de la fuente, tamaño y estilo, la fuente a utilizar en el texto del componente. Por ejemplo, Font(“Times New Roman”, 24, “bold underline”).
bd: modificamos la anchura del borde del widget.
relief: cambiamos el estilo del borde del componente. Su valor puede ser “flat”, “sunken”, “raised”, “groove”, “solid” o “ridge”.
state: permite deshabilitar el componente (state=DISABLED); por ejemplo, una Label en la que no se puede escribir o un Button que no se puede clickar.
padding: espacio en blanco alrededor del widget en cuestión.
command: de cara a que los botones hagan cosas, podemos indicar qué función ejecutar cuando se haga click en el mismo.
5. Gestión de la composición
Es MUY IMPORTANTE que, cuando tengamos configurado el componente, utilicemos un gestor de geometría de componentes. Si no, el widget quedará creado pero no se mostrará.

Los tres más conocidos son:

Pack: cuando añadimos un nuevo componente, se “hace hueco” a continuación de los que ya están incluidos (podemos indicar que se inserte en cualquiera de las 4 direcciones), para finalmente calcular el tamaño que necesita el widget padre para contenerlos a todos.
Place: este es el más sencillo de entender, pero puede que no el más sencillo de utilizar para todo el mundo. Al insertar un componente, podemos indicar explícitamente la posición (coordenadas X e Y) dentro del widget padre, ya sea en términos absolutos o relativos.
Grid: la disposición de los elementos es una matriz, de manera que para cada uno debemos indicar la celda (fila y columna) que queremos que ocupe. Podemos además especificar que ocupe más de una fila y/o columna (rowspan/columnspan=3), “pegarlo” a cualquiera de los 4 bordes de la celda en vez de centrarlo (sticky=W para el borde izquierdo, por ejemplo)…
Personalmente, me siento mucho más cómodo utilizando un Grid: de esta manera te aseguras la distribución de los componentes, y la hora de añadir nuevos es muy visual poder pensar en ello como matriz, en vez de coordenadas o posiciones relativas a otros widgets.

6. Ejecución
Una vez tenemos todos los componentes creados, configurados y añadidos en la estructura, debemos terminar el script con la instrucción tk.mainloop() (“tk” = variable Tk). Así, cuando lo ejecutemos, se abrirá la ventana principal de nuestra GUI.

Bricotruco: si guardamos nuestro script con formato .pyw en vez de .py, al ejecutarlo se abrirá nuestra interfaz, sin tener que pasar por terminal o abrir algún IDE para ello.

