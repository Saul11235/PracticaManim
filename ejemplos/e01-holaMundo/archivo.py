#importa todos los contenidos de la libreria manim
from manim import *

#crearemos una nueva clase que herede de Scene
class HolaMundo(Scene):
    #definimos la funcion construct 
    def construct(self):
        #creamos objeto tipo Text
        texto=Text("Hola Mundo",font_size=144)
        #colocamos en el objeto padre
        self.add(texto)




