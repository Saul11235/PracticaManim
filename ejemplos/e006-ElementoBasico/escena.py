#ejemplo de los elementos basicos de manim

from manim import *

class PrimeraEscena(Scene):
    def construct(self):  # toda escena debe tener un metodo construct
        #codigo para crear
        texto=Text("Hola soy\nla primera\nEscena",font_size=54 )
        #animamos con un FadeIN
        self.play(FadeIn(texto))
        self.play(FadeOut(texto))


class SegundaEscena(Scene):
    def construct(self):  # toda escena debe tener un metodo construct
        #codigo para crear
        texto=Text("Hola soy\nla segunda\nEscena\nEstoy en ESPAÑOL",font_size=64 )
        #animamos con un FadeIN
        self.play(FadeIn(texto))
        self.play(FadeOut(texto))




