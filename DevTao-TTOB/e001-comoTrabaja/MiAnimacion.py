from manim import *

class MiEscena(Scene):
    def construct(self):
        #definir objs
        circulo=Circle()
        #animaciones
        self.play(GrowFromCenter(circulo))
        self.wait()
        pass
