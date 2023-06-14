import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("Este código plota o gráfico de uma função de duas variáveis e suas curvas de nível.")

# pede para digitar o intervalo de x e y
x_min = float(input("Digite o valor mínimo de x: "))
x_max = float(input("Digite o valor máximo de x: "))
y_min = float(input("Digite o valor mínimo de y: "))
y_max = float(input("Digite o valor máximo de y: "))

# pede para digitar a função de duas variáveis
print('\nUtilize desta forma Função A: -x*y*np.exp(-x**2 - y**2)\n Função B: np.sin(x*y)')
funcao = input("Digite a função de duas variáveis: ")

# define a função de duas variáveis
def f(x, y):
    return eval(funcao)

# cria o grid de pontos
num_points = 100
x_vals = np.linspace(x_min, x_max, num_points)
y_vals = np.linspace(y_min, y_max, num_points)
x, y = np.meshgrid(x_vals, y_vals)

# calcula os valores de z para cada ponto do grid
z = f(x, y)

# plota o gráfico de superfície da função
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
ax.set_title('Gráfico 3D')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# ajusta o intervalo de z para garantir cores uniformemente distribuídas
z_min, z_max = np.min(z), np.max(z)
ax.set_zlim(z_min, z_max)
ax.zaxis.set_ticks(np.linspace(z_min, z_max, 5))

plt.savefig('superficie.png')
plt.show()

# plota as curvas de nível da função
plt.contour(x, y, z, cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('curvas_de_nivel.png')
plt.show()
