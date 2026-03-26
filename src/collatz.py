import matplotlib.pyplot as plt

# función de collatz
def collatz(n):
    pasos = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1

    return pasos


# listas para el gráfico
numeros = []
iteraciones = []

# calcular para 1 a 10000
for i in range(1, 10001):
    numeros.append(i)
    iteraciones.append(collatz(i))

# gráfico
plt.scatter(iteraciones, numeros, s=1)

plt.title("Conjetura de Collatz")
plt.xlabel("Cantidad de iteraciones")
plt.ylabel("Número inicial")

plt.show()