from manim import *

# VIDEO:-ql -qm -qh VIDEO-PREV -pql -pqm -pqh FRAME: -s -ps
OPCIONES="-pql"
ESCENAS="MiEscena"

class MiEscena(Scene):
    def construct(self):
        #definir objs
        circulo=Circle()
        #animaciones crear circulo desde el centro
        self.play(GrowFromCenter(circulo))
        #espera 
        self.wait()

#=======================================
#=======================================
#=======================================
# ejecucion automatica Manim
if __name__=="__main__":
    from os import system
    NombreArchivo=str(__file__)
    OPCIONES2="";ESCENAS2=""
    try:OPCIONES2=OPCIONES
    except:pass
    try:ESCENAS2=ESCENAS
    except:pass
    system("manim "+NombreArchivo+" "+OPCIONES2+" "+ESCENAS2)
#=======================================
#=======================================
#=======================================
