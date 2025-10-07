import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')  # Backend interactivo Qt5 para mostrar gráficos
import matplotlib.pyplot as plt
import Equation
#Crear los datos del campo de pendientes ... Seleccionar un rango razonable de temperaturas (por ejemplo, 60°F a 100°F) y tiempos (0 a 5 h).
#

t_vals = np.linspace(0, 5, 20) # Crea un array con 20 valores uniformemente distribuidos desde 0 hasta 5 (tiempo en horas).
T_vals = np.linspace(60, 100, 20) # Lo mismo para temp de 0 a 60 F.
T, t = np.meshgrid(T_vals, t_vals) # Cuadricula, te hace el grid combinando T con t.


dTdt = Equation.f(T)

#Dibujar el campo de direcciones (isoclinas)

#Líneas azules inclinadas hacia abajo: indican que 𝑇 disminuye si es mayor que 70.
#Líneas horizontales cerca de 70: muestran que ahí la derivada es 0 → equilibrio.
#El campo de pendientes apunta hacia el equilibrio, confirmando que es estable.

plt.figure(figsize=(8,6))
plt.quiver(t, T, np.ones_like(dTdt), dTdt, color="blue")
plt.title("Campo de pendientes e isoclinas de la Ley de Newton")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Temperatura (°F)")
plt.axhline(70, color="red", linestyle="--", label="Equilibrio (70°F)")
plt.legend()
plt.show()

#Agregar la solución real sobre el campo (opcional y útil)
t_line = np.linspace(0, 5, 100)
T_line = Equation.Ta + 10 * np.exp(-k * t_line)

plt.figure(figsize=(8,6))
plt.quiver(t, T, np.ones_like(dTdt), dTdt, color="lightgray")
plt.plot(t_line, T_line, color="red", linewidth=2, label="Solución analítica")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Temperatura (°F)")
plt.title("Solución analítica y campo de pendientes")
plt.axhline(70, color="black", linestyle="--", label="Equilibrio 70°F")
plt.legend()
plt.show()