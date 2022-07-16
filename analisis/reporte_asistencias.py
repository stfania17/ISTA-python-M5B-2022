import pandas as pd
import matplotlib.pyplot as plt
import csv

datosestu = pd.read_csv('datos\estudiante.csv')

print('ESTUDIANTES')
print(datosestu)

datosestu1 = pd.read_csv('datos\datos_asistencia.csv')

print('ASISTENCIAS')
print(datosestu1)

estudent = pd.merge(datosestu,datosestu1, how='right')
print(estudent)

print('ESTUDIANTES POR CEDULA = 1161310234')
print(estudent[estudent.cedula == 1161310234])

estudent[estudent.cedula == 1161310234].to_csv('datos\datos_reporte_1161310234.csv', index=True)

estudent[estudent.cedula == 1161310234]['fecha_dia'].value_counts().plot(kind='bar')

plt.show()

