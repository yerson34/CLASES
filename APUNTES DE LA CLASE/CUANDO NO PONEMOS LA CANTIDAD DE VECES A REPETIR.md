### *CUANDO NO PONEMOS LA CANTIDAD DE VECES A REPETIR*

```PYTHON
condicion=True
        while condicion:
        print("hola")
        texto=input("ingresa tu nombre o salir para terminar elprograma:")
        if texto=="salir":
        condicion=false
 ```
   
### *3-.crear un programa que me pida 5 veces un nombre y por cada vez que lo pida muestre la cantidad de veces que ingreso el nombre*
```python
nombres = {}
contador = 0`

while contador < 5:
    nombre = input("Ingresa un nombre: ")
    
    if nombre in nombres:
       nombres[nombre] += 1
    else:
        nombres[nombre] = 1
    
    contador += 1
```

### *4 crear un programa que pida un numero y lo evalue con el numero premiado si el numero ingresado es el premiado el programa finalizara si el numero ingresado es incorrecto el programa seguira pidiendo el numero premiado*
 ```python
numero_premiado = 1234

for i in range(3):
    numero = int(input("Ingresa un número: "))
    
    if numero == numero_premiado:
        print("¡Felicidades! Has ingresado el número premiado.")
        break
    else:
        print("Número incorrecto. Sigue intentando.")
```
  ## FUNCIONES 
  ### *EXITEN DOS TIPOS DE FUNCIONES*
 FUNCIONNES PROPIAS DEL LENGUAJE
 QUE YA BIENEN CREADAS E INSERTADAS EN PYTHON Y ESTAN LISTAS PARA SER USADAS 
 EJEMPLO
 DENTRO DE LAS PARENTISES PODREMOS PASARLE DATOS  QUE NECESITA PARA EJECUTAR.
 print()
 ESTA SIRVE PARA MOSTRAR POR CONSOLA DATOS 
 
FUNCIONES CREADAS
