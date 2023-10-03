# 1. TIPOS DE DATOS

* *TIPOS DE DATOS PRIMITIVOS.* 

* *'a' string cadena de texto*

* *'hola' esto tambien es un string*

* *'hola soy un strig y te saludo' cadena larga*

#### OBSERVACIÓN: todo lo que este entre comillas es un string 

### un string puede estar entre comillas simples o dobles 

*  "100" Este es un tipo de dato númerico entero* 

*  "2.1" Este es un tipo de dato numerioc flotante*


*  "False" Este es un tipo de dato boleano falso* 


*  "true" Tipo de dato boleano verdadero*

## 2. variables
 
* *Es donde almacenamos nuestros tipos de datos.*

* *Esos datos pueden mutar o ccambiar o modificarse.*

* *Como creamos una variable para almacenar nuestros datos.*

* *Darle un nombre significante o realacionado al dato que estamos almacenando.*

* Indicarle a que dato esta asociado -> asignacion 

* Indicar el tipo de dato que se va a almacenar -> darle al dato a guadar.

**EJEMPLOS**

 * Primero al dato voy a pedir la edad de nadine 

     edad_nadne=18

 * El nombre de un alumno 

     nombre_alumno=edwin


## 3.Operadores 
### **Operados aritmeticos** 
* **SUMA**  (+)

* **RESTA** (-) 

* **MULTIPLICACION** (*) 

* **DIVISION** (/)

**SUMA**

**suma=45+12**

**RESTA**

**resta=34-12**

**MULIPLICACION**

**multi=3x4**

**DIVICION**

**division=2/4**

**OPERACION=(45+12+23)/4**

**OP=15+12+14+13/4**
## 4.datos estructurados

#### Listas
* Puede alamcenar distintos tipos de datos en una sola lista 
```python
     ['nombre',10,False]
     lista_amigos=['jori','edwin','adan','chinita']
```
#### Objetos
* tambien al igual que las listas almacenan distintos tipos de datos pero son un orden
* para almacenar datos en un objeto necesitamos especificar un inidce y un valor clave->valor
```python
alumno={
    'nombre':'jori'
    'edad':52',
    'sexo':'todos los dias'
```
#### Combinar ambas estructuras de datos 
 ```python
alumno={
    'nombre' : 'jori'
    'edad':30,
    'amigos':['antony','edwin','china']
'direccion': {
    'departamento':'ayacucho'
    'provincia':'lucanas'
    'distrito':'puquio'
    'jiron':'san peter'
    'numero':152 
 }
}
```
## 5. funciones

### Controles de flujos 

* solo se ejecuta si cumple o si elas condicion es verdadera podemos hacere que si condicion es false se ejecute otro codigo  
### Deciciones 

* expecifica el codigo que se ejecutara si se cumple una condicion 

```python 
if <condicion:
```
* el codigo que deseamos ejecutar si la condicxion es verdad 
```python
print ("ejecuta esto")
```
* aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende.
```python
print("esto siempre ejecutara ")
```
* si queremos que se ejecute un codigo en caso sea falsa
```python 
if <condicion falsa >:
print("solo imprime si es verdad 
else :
print("solo imprime  si es falso")
```
### Ejemplo 
```python
if 15>18
print("si es verdad imprime esto ")
else:
print(" si es verdad falso imprime esto ")
```
########################################
```python
if 15*2==30
print(si es verdad imprime esto" )
else:
print(" si es falso imprime esto")
```
########################################
```python
condicion=true
if condicion:
print("si es verdad imprime esto") 
else:
print(" si es falso imprime esto")
```
### ciclos 
* Existen dos tipos 
* Cuando sabes la cantidad de veces 
* Sintaxis despues d3e la palabra reservada for deberemos crear una variable que * Almacene el numero que iremos iterando .

* Luego tendremos que interar a los elementos e iterar 
```python
VOCALES=["A","E","I","o","U"]
for i in range(i,5)
print(i)
```
* Cuando no sabemos la cantidad de veces a repetir.

##  Esta funcion nos muestra el numero mayor de una lista 

* lista=(45;12:78;)
* numero mayor y mernor 
* print ( numero menor )
* funcion para convertir de un string a un numero entero 

```PYTHON
numro_string_"100"
print(type(numero_string))
numero_entero =int(numero_string)
```
* funcion para convertir un numero entero a un string

* str (100) # ->> "100" -> string
* funciones de python que nos permite agregar elementos al final de una linea
 * se encuentra al final de una lista 

 ```PYTHON

LISTA=(12;23:34)
LISTA.pop()
PRINT(LISTA)
```
## INSERT
Funcion de python  que nos permite agregar elementos en cualquier posicion de una lista es se le tiene que pasar dos parametro, primero indiacarle el indice y segundo el dato que se va agregar.
python
Ejemplo:

lista_nombres=['jory','nadine','bichota']
lista_nombre.insert(1,'satan')
print(lista_nombres)

## Remove
Funcion de python que nos permite eliminar  elementos de cualquier posicion de una lista, esta funcion recibe solo el elemento que deseamos eliminar.
python
Ejemplo:

lista=[4,5,6,7,8,]
lista.remove(6)
print(lista)

## SPLIT
Funcion que nos permite dividir en una lista una cadena.
python
Ejemplo:

cadena='Hola como estan'
lista=cadena.split()
print(lista)
url='wwww.google.com/id=70133573
id=url.split('=').pop()
print(id)
## 2. definir un nombre de funcion que describa que tarea va a realizar.
* una funcion son mini programas tobbien se le comoce como modulos o fragmentos de codigo de uso exclusivo funciones propias

## 3. establecer los parametros que resivira la funcion entre parentesis (). I
* #pasos para crear una funcion propia

* 1. hacer uso de la palabra reservada def.
* 2. definir un nombre de funcion que describa que tarea va a realizar

 * para retornar un mensaje en nuestra funcion. ax existen dos tipos de funciones los que no resiven ningun parametro y los que resiven parametros


 ## 4. establecer que valor o dato va retornar mi funcion con la palabra reservada return 
### Observacion =>> tambien podemos hacer uso de la funcion print () para retornar un mensaje en nuestra funcion.

* como hacemos uso de la funcion??

* nombre de la funcion y parentesis
* funcion con parametros 
```python 
def salude():
```
* print(Chola este es un saludo')

* mi print ("ola esto es un print de python " )
```python

def suma(a;b):
total=)a+b
return
mi print(suma(45,12))##->>57
```
## ssEjemplo:
```python



lista=[12,4,45,3,78,1]
mi-print(max(lista)) ---->> 78


def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
            numero_mayor=numero
     return numero_mayor
mi_print(mi_max(lista))
```



### FUNCIONES CREADAS 
