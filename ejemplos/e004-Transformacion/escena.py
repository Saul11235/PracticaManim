# ejemplo obtenido de:
# https://docs.manim.community/en/stable/tutorials/quickstart.html

from manim import *

class TransformacionCuadradoAcirculo(Scene):

    def construct(self):
        #creando objeto circulo y configurando
        circulo= Circle()
        circulo.set_fill(PINK, opacity=0.5)
        #creando objeto cuadrado y rotando pi/4 radianes
        cuadrado= Square()
        cuadrado.rotate(PI / 4)
        #---------------------+
        #  ZONA DE ANIMACION  |
        #---------------------+
        self.play(Create(cuadrado))  #crear cuadrado
        #interpolar elementos para transformar de cuadrado a circulo
        self.play(Transform(cuadrado, circulo))  
        self.play(FadeOut(cuadrado))  # desaparecer cuadrado
