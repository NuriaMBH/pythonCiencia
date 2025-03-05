import matplotlib.pyplot as plt
#LA MAYORIA DE LOS GRAFICOS SULEN TENER DOS EJES DE COORDENADAS PARA REPRESENTAR SUS DATOS(X,Y)
x = ['Betis','Atletico del madrid','Barcelona','Real Madrid']
#VALOR DEL MERCADO
y = [5,10,15,20]

#CREAMOS EL GRAFICO MEDIANTE plt Y CON UN METODO IREMOS INDICANDO
#EL TIPO DE GRAFICO QUE QUEREMOS
#BARRAS
plt.bar(x,y)
#PERSONALIZAREL GRAFICO
plt.title("Grafico de Barras")
plt.xlabel("Equipos")
plt.ylabel("valor del Marcado")
#podemos almacenar el grafico en una imagen
plt.savefig('images/barras.png')
plt.show()