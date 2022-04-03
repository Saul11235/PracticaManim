#ejemplo sacado de la documentacion oficial de manim
#https://docs.manim.community/en/stable/tutorials/quickstart.html

from manim import *

class cuadradoYcirculo(Scene):
    def construct(self):
        #creando circulo=Circle() y configurando
        circulo=Circle()  
        circulo.set_fill(PINK, opacity=0.5)
        #creando cuadrado=Square() y configurando
        cuadrado=Square() 
        cuadrado.set_fill(BLUE, opacity=0.5) 
        # colocando  cuadrado a la derecha cel circulo
        cuadrado.next_to(circulo, RIGHT, buff=0.5)  
        #animando y colocando los dos objetos en pantalla
        self.play(Create(circulo), Create(cuadrado))  
