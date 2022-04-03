#esto es un ejemplo que lanza un  comando en la terminal de comandos
#lanza el comando:
# Nota: se debe definir antes manim como comando del sistema
#
#
#  +--------------------------------------+
#  |                                      |
#  |  manim  -pql  ejemplo.py  HolaMundo  |
#  |                                      |
#  +--------------------------------------+
#
#  manim      : comando manim
#  -pql       : argumento pql para manim
#  ejemplo.py : script python con codigo 
#  HolaMundo  : clase heredera de manim.Scene para renderizar
#

from os import system

system("manim -pql archivo.py HolaMundo")


