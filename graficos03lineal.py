import matplotlib.pyplot as plt
#LA MAYORIA DE LOS GRAFICOS SULEN TENER DOS EJES DE COORDENADAS PARA REPRESENTAR SUS DATOS(X,Y)
x = ['Betis','Atletico del madrid','Barcelona','Real Madrid']
#VALOR DEL MERCADO
y = [5,2,15,20]

#CREAMOS EL GRAFICO MEDIANTE plt Y CON UN METODO IREMOS INDICANDO
#EL TIPO DE GRAFICO QUE QUEREMOS
#LINEAL
plt.plot(x,y)
#PERSONALIZAREL GRAFICO
plt.title("Grafico de Lineas")
plt.xlabel("Equipos")
plt.ylabel("valor del Mercado")
#podemos almacenar el grafico en una imagen
plt.savefig('images/lineal.png')
plt.show()