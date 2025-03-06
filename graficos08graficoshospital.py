import oracledb

import matplotlib.pyplot as plt

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Graficos Doctores por Hospital")
hospitales= []
personas= []

cursor = connection.cursor()
sql = """
cursor = connection.cursor
select * from DOCTOR;
select * from HOSPITAL;
select count (DOCTOR.DOCTOR_NO) AS personas
, HOSPITAL.NOMBRE
from DOCTOR
inner join HOSPITAL 
ON DOCTOR.HOSPITAL_COD = HOSPITAL.HOSPITAL_COD 
GROUP BY HOSPITAL.NOMBRE """
cursor.execute(sql)
for numero, nombre in cursor:
    hospitales.append(nombre)
    personas.append(numero)
cursor.close()
connection.close()
plt.pie(personas, labels=hospitales)
plt.title("Doctores por hospital")
plt.show()