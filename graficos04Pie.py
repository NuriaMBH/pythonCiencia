import matplotlib.pyplot as plt
#LA MAYORIA DE LOS GRAFICOS SULEN TENER DOS EJES DE COORDENADAS PARA REPRESENTAR SUS DATOS(X,Y)
etiquetas = ['Betis','Atletico del madrid','Barcelona','Real Madrid']
#VALOR DEL MERCADO
valores = [5,2,15,20]

plt.pie(valores, labels=etiquetas)
plt.title("Gráfico de Tarta")
plt.savefig('images/cirsular.png')
plt.show()