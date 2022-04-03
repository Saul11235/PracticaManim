# ejemplo adaptado de 
# https://docs.manim.community/en/stable/tutorials/quickstart.html

from manim import *

class RotacionesDiferentes(Scene):
    # consiste en dos cuadrilateros cuadradoIzq y cuadradoDer
    # estos tendran dos formas diferentes de rotar
    def construct(self):
        #creando y definiendo objetos cuadrado
        cuadradoIzq=Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        cuadradoDer=Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        #configurando animacion
        self.play(
            cuadradoIzq.animate.rotate(PI), Rotate(cuadradoDer, angle=PI), run_time=2
        )
        self.wait()
