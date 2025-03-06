import oracledb
import matplotlib.pyplot as plt
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Graficos con BBDD")

sql = "select OFICIO, AVG(SALARIO) as MEDIA from EMP group by OFICIO"


oficios= []
medias = []
cursor= connection.cursor()
cursor.execute(sql)
for row in cursor:
     oficios.append(row[1])
     medias.append(row[1])
   
cursor.close
plt.pie(medias,labels=oficios)
plt.title("Grafico media salarial EMP")
plt.show()