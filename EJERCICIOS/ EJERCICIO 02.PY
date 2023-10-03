#El NOMBRE SIEMPRE DEBERIA SER EN SINGULAR Y CON LA PRIMERA LETRA MAYUSCULA 
class perro:
     nombre ="boby"
     edad="2 meses"
     color="rojo"
     raza="chusco"

     def ladrar(self):
          return "gua gua gua mascota"
     def corre (self,paso):
          huevo=f"corriste (pasos)"
          return huevo
        
respuesta=perro()
print(respuesta.nombre)
print(respuesta.ladrar())
print(respuesta.color)
print(respuesta.raza)
print(respuesta.edad)
