import euler
import euler_mejorado
import rugge_kutta
#usamos una edo con solucion analitica como y'=x+y que es y=x^2/2+k para k=0 nos queda y=x^2/2 si evaluamos en x=0,y=0 en x=1,y deberia ser =1/2
#comprobemos
class Punto:
    x:float
    y:float
    def __init__(self,x,y):
        self.x=x
        self.y=y
punto=Punto(0,0)
x_final=1
paso=1
orden_rugge_kutta=4
T = 80
solucion_euler=euler.calcular_punto_con_euler(punto,x_final,edo,paso)
solucion_euler_mejorado=euler_mejorado.calcular_punto_con_euler_mejorado(punto,x_final,edo,paso)
solucion_rugge_kutta=rugge_kutta.calcular_punto_con_rugge_kutta(punto,x_final,edo,paso,orden_rugge_kutta)
