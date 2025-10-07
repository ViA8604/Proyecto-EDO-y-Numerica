from math import isclose
#definimos un punto como un diccionario con x y y
#la edo es una funcion f(x,y)
def edo(x,y):
    #aqui ponemos nuestra edo por ejemplo y'=x+y
    return x+y
#necesito un punto inicial (x,y) de la funcion original, el punto a donde quiero calcular su y, la edo y el paso
def calcular_punto_con_euler_mejorado(punto,x_final,edo,paso):
    nuevo_punto=punto
    while not isclose(nuevo_punto.x,x_final):
        m=calcular_m_promedio_con_x_final(edo,x_final,nuevo_punto)
        n=nuevo_punto.y-(m*nuevo_punto.x)
        #aqui tenemos la ecuacion de la recta en ese punto y=mx+n
        nuevo_punto.x=nuevo_punto.x+paso
        #hallamos y
        nuevo_punto.y=m*nuevo_punto.x+n
    return nuevo_punto
#para calcular m debemos hallar el promedio con su x_final
def calcular_m_promedio_con_x_final(edo,paso,punto):
     x2=punto.x+paso
     m1=edo(punto.x,punto.y)
     n1=punto.y-m1*punto.x
     #aqui tenemos la ecuacion de la recta en ese punto
     y_final=m1*x2+n1
     #tenemos el supuestamente punto final
     m2=edo(x2,y_final)
     return (m1+m2)/2
