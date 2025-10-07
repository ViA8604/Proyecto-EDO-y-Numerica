from math import isclose
#definimos un punto como un diccionario con x y y
#la edo es una funcion f(x,y)
def edo(x,y):
    #aqui ponemos nuestra edo por ejemplo y'=x+y
    return x+y
#necesito un punto inicial (x,y) de la funcion original, el punto a donde quiero calcular su y, la edo y el paso
def calcular_punto_con_euler(punto,x_final,edo,paso):
    nuevo_punto=punto
    while not isclose(nuevo_punto.x,x_final):
        m=edo(nuevo_punto.x,nuevo_punto.y)
        n=nuevo_punto.y-(m*nuevo_punto.x)
        #aqui tenemos la ecuacion de la recta en ese punto y=mx+n
        nuevo_punto.x=nuevo_punto.x+paso
        #hallamos y
        nuevo_punto.y=m*nuevo_punto.x+n

    return nuevo_punto

class Punto:
    x:float
    y:float
    def __init__(self,x,y):
        self.x=x
        self.y=y
punto=Punto(0,0)
x_final=1
paso=0.1
orden_rugge_kutta=4
def edo(x,y):
    return x
calcular_punto_con_euler(punto,x_final,edo,paso)