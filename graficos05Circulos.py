# graficos de circulos
# necesito un nombre del comercial y sus ventas de producto
# mostraremos un grafico circular con los productos y sus ventas
# necesitamos representar productos y sus ventas
# necesito pedir al usuario los datos input() y vamos rellenando el producto y las ventas.
# pedimos 5 datos y despues dibujamos el grafico
import matplotlib.pyplot as plt

productos = []
ventas = []
print("Nombre del Comercial")
comercial = input()
for i in range(5):
    print("Nombre del producto")
    prod = input()
    print("Número de ventas") 
    num = int(input())
    productos.append(prod)
    ventas.append(num)  
plt.pie(ventas,labels=productos)
plt.title(f"Comercial: {comercial}")
plt.show()


