import matplotlib.pyplot as plt

# datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# crear gráfico
plt.plot(x, y)

# títulos
plt.title("Gráfico de Línea")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# mostrar gráfico
plt.show()