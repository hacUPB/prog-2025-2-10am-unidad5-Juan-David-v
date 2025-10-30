import math
import matplotlib.pyplot as plt
import numpy as np

# Datos
#x = np.linspace(0, 10, 100)
#y = np.sin(x)
x=[1,3,5,7,9,11,13]
y=[2,3,4,7,8,12,34]
for i in range (100):
    x.append(i)
for j in range (100):
    y.append(math.cos(2*math.pi*x[j]))
# Crear la gráfica
plt.plot(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Coseno')
plt.xlabel('X')
plt.ylabel('cos(X)')

# Mostrar la gráfica
plt.show()