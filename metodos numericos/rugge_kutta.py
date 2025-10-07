from math import isclose
#definimos un punto como un diccionario con x y y
#la edo es una funcion f(x,y)
def edo(x,y):
    #aqui ponemos nuestra edo por ejemplo y'=x+y
    return x+y
#necesito un punto inicial (x,y) de la funcion original, el punto a donde quiero calcular su y, la edo,el orden del rugge kutta y el paso
def calcular_punto_con_rugge_kutta(punto,x_final,edo,paso,rugge_kutta_orden):
    nuevo_punto=punto
    while not isclose(nuevo_punto.x,x_final):
        m=calcular_m_promedio_con_orden(edo,nuevo_punto,paso,rugge_kutta_orden)
        n=nuevo_punto.y-(m*nuevo_punto.x)
        #aqui tenemos la ecuacion de la recta en ese punto y=mx+n
        nuevo_punto.x=nuevo_punto.x+paso
        #hallamos y
        nuevo_punto.y=m*nuevo_punto.x+n
    return nuevo_punto
#para calcular m debemos hallar el promedio con su x_final
def calcular_m_promedio_con_orden(edo,punto,paso,rugge_kutta_orden):
     m1=edo(punto.x,punto.y)
     n1=punto.y-m1*punto.x
     #aqui tenemos la ecuacion de la recta en ese punto ahora calculamos los demas puntos
     puntos=[punto]
     for i in range(1,rugge_kutta_orden):
         punto_x=punto+paso*i
         punto_y=punto_x*m1+n1
         puntos.append({'x':punto_x,'y':punto_y})
     ms=[m1]
     for i in range(1,rugge_kutta_orden):
         ms.append(edo(puntos[i].x,puntos[i].y))
     suma=0
     for i in range(rugge_kutta_orden):
         suma+=ms[1]
         
     return suma/rugge_kutta_orden
           