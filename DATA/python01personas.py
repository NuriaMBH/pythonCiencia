import pandas as pd
print("Hola Mundo")

#vamos a crear un diccionario con elementos que se llaman SERIES
#NO DEJA DE SER UN DICCIONARIO con valores que van correspondientes entre 
#ellos, aunque prodrían no ser correspondientes

datos = {
    'nombres':['Lucía','Andrea','Alex','Antonia'],
    'edad' : [22,17,48,70],
         'ciudad':['Segovia','Parla','Madrid','Toledo']
         }

#Almacenamos los datos en un dataframe
df = pd.DataFrame(datos)
print(df)

#Podemos filtrar los datos de un dataframe
#la forma de filtrar es mediante la siguiente sintaxis:
#df[ de[COLUMNA]==valor]
print("dataframe filtrado-------")
df_filtrado = df[df['edad'] > 30]
print(df_filtrado)
print("-------Dataframe ordenado---------")
#podemos ordenar por una o varias columanas
# df.sort_values(COLUMNA)
df_sorted = df.sort_values('edad')
print(df_sorted)