# necesito visualizar un graficos lineal(plot) de temperatura de cada día de la semana
# pediremos la temperatura de cada día
# ltemperatura lunes: 3
# temperatura martes:14
# temperatura miercoles:7
import matplotlib.pyplot as plt
#listas para almacenar los días y las temperaturas
semana = ("lunes","Martes","Miercoles","jueves","Viernes","sabado","Domingo")
temperaturas = []
#REALIZAMOS UN BUCLE PARA RELLENAR LOS DATOS

for i in range(len(semana)):
    print(f"Introduzca temperatura para {semana[i]}")
    temp = int (input())
    temperaturas.append(temp)
       
plt.plot(semana, temperaturas, labels= "Semana 1")
#PODEMOS INCLUIR MAS DATOS DENTRO DEL GRAFICO LINEAL
#SIEMPRE QUE PONGAOS UN LABEL A CADA plot()
temperaturas2 = [5,20,8,12,19,22,30]
plt.plot(semana,temperaturas2, labels="Semana 2")
plt.title(f"Temperatura Semana 1 de marzo")
plt.xlabel("Día de la semana")
plt.ylabel("Temperatura")
plt.show()