# ejemplo de la doc oficial de manim, el script lanzar 
# coloca el comando en pantall
# https://docs.manim.community/en/stable/tutorials/quickstart.html

#importamos todo el contenido del paquete manim
from manim import *

class crearCirculo(Scene): #creamos una clase llamada crearCirculo
    #definimos dentro de la clase la funcion construct(self)
    def construct(self):
        circulo=Circle()   #crear objeto 'circulo' tipo Circle
        #configurando objeto con manim.YELLOW 
        circulo.set_fill(YELLOW, opacity=0.5) 
        self.play(Create(circulo))#mostrar circulo en pantalla
