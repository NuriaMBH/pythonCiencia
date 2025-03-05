# necesito visualizar un graficos lineal(plot) de temperatura de cada día de la semana
# pediremos la temperatura de cada día
# ltemperatura lunes: 3
# temperatura martes:14
# temperatura miercoles:7
import matplotlib.pyplot as plt

dia = []
temperatura = []
print("Temperatura Semanal para el mes ")
mes = input()
for i in range(5):
    print("Día de la semana")
    prod = input()
    print("grados")
    num = int(input())
    dia.append(prod)
    temperatura.append(num)
plt.plot(temperatura, labels=dia)
plt.title(f"Temperatura: {mes}")
plt.show()